"""匹配引擎：兼容性硬门槛 + 成本/利润/效率三维打分（初始版，零依赖）。"""

from datetime import datetime

# 兼容性作为硬门槛（不兼容直接排除）；在兼容候选中按这三项加权排序。
WEIGHTS = {"cost": 0.45, "profit": 0.20, "efficiency": 0.35}


def _days_until(date_str):
    try:
        return (datetime.fromisoformat(str(date_str)) - datetime.now()).days
    except Exception:
        return 30


def _normalize_higher_is_better(vals):
    """值越小越好 -> 归一化为越高越好。"""
    mn, mx = min(vals), max(vals)
    if mx == mn:
        return [1.0 for _ in vals]
    return [round((mx - v) / (mx - mn), 4) for v in vals]


def _compatible(required, specs):
    """需求关键字的所有 token 都出现在供给 specs 中才视为兼容。"""
    if not required:
        return True
    req_tokens = set(str(required).lower().split())
    spec_tokens = set(str(specs).lower().split())
    return req_tokens.issubset(spec_tokens)


def _raw(demand, supply):
    quantity = int(demand.get("quantity", 1))
    price = float(supply.get("price", 0))
    budget = float(demand.get("budget", 0)) or 1.0
    lead_time = int(supply.get("leadTime", 30))
    moq = int(supply.get("moq", 0))
    days = _days_until(demand.get("deadline", ""))
    required = demand.get("components", {}).get(supply.get("category", ""), "")

    lead_ok = lead_time <= max(days, 0)
    moq_ok = moq <= quantity
    return {
        "cost_raw": price * quantity,          # 总成本，越低越好
        "profit_raw": (price * quantity) / budget,  # 占预算比例，越低利润空间越大
        "efficiency": ((1.0 if lead_ok else 0.0) + (1.0 if moq_ok else 0.0)) / 2.0,
        "compatible": _compatible(required, supply.get("specs", "")),
        "lead_ok": lead_ok,
        "moq_ok": moq_ok,
    }


def match(demand, supplies):
    """按需求类别分组；先按兼容性硬过滤，再在兼容候选中打分排序。"""
    by_cat = {}
    for s in supplies:
        by_cat.setdefault(s.get("category", ""), []).append(s)

    matches_by_category = {}
    recommended = []
    for cat in demand.get("components", {}).keys():
        cands = by_cat.get(cat, [])
        if not cands:
            matches_by_category[cat] = []
            continue

        compat, excluded = [], []
        for s in cands:
            r = _raw(demand, s)
            (compat if r["compatible"] else excluded).append((s, r))

        ranked = []
        if compat:
            cost_n = _normalize_higher_is_better([r["cost_raw"] for _, r in compat])
            profit_n = _normalize_higher_is_better([r["profit_raw"] for _, r in compat])
            for i, (s, r) in enumerate(compat):
                dims = {
                    "cost": cost_n[i],
                    "profit": profit_n[i],
                    "efficiency": round(r["efficiency"], 2),
                    "compatibility": 1.0,
                }
                score = sum(WEIGHTS[k] * dims[k] for k in WEIGHTS)
                ranked.append({
                    "supply": s,
                    "score": round(score, 3),
                    "dimensions": dims,
                    "reasons": _reasons(s, r),
                    "excluded": False,
                })
            ranked.sort(key=lambda x: (-x["score"], x["supply"]["price"]))

        for s, r in excluded:
            ranked.append({
                "supply": s,
                "score": 0.0,
                "dimensions": {"cost": 0.0, "profit": 0.0, "efficiency": round(r["efficiency"], 2), "compatibility": 0.0},
                "reasons": ["规格不匹配，已排除"],
                "excluded": True,
            })

        matches_by_category[cat] = ranked
        if ranked and not ranked[0]["excluded"]:
            recommended.append(ranked[0]["supply"]["id"])

    return {"matches_by_category": matches_by_category, "recommendedGroup": recommended}


def _reasons(s, r):
    reasons = ["规格匹配"]
    reasons.append("交期" + ("满足" if r["lead_ok"] else "偏长"))
    reasons.append("MOQ" + ("满足" if r["moq_ok"] else "不满足"))
    reasons.append("单价" + str(s.get("price")))
    return reasons
