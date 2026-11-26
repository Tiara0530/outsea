"""Outsea 客商对接智能系统 —— 后端初始版（零依赖，Python 标准库）。

启动服务：  python main.py
演示流程：  python main.py --demo
"""

import json
import sys
import uuid
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

import data as sample_data
import matching

DEMANDS = {}
SUPPLIES = {}
CONNECTIONS = {}


def _load_samples():
    d = sample_data.DEMAND_JIA
    DEMANDS[d["id"]] = dict(d)
    for s in sample_data.SUPPLIES:
        SUPPLIES[s["id"]] = dict(s)


def _ok(data, msg="ok"):
    return {"code": 0, "message": msg, "requestId": uuid.uuid4().hex[:8], "data": data}


def _err(msg, code=40001):
    return {"code": code, "message": msg, "requestId": uuid.uuid4().hex[:8], "data": None}


class Handler(BaseHTTPRequestHandler):
    def _send(self, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            return json.loads(raw.decode("utf-8"))
        except Exception:
            return {}

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/v1/health":
            return self._send(_ok({"status": "up", "demands": len(DEMANDS), "supplies": len(SUPPLIES)}))
        if path.startswith("/api/v1/match/"):
            return self._match(path.rsplit("/", 1)[-1])
        if path == "/api/v1/demands":
            return self._send(_ok(list(DEMANDS.values())))
        if path == "/api/v1/supplies":
            return self._send(_ok(list(SUPPLIES.values())))
        if path == "/api/v1/connections":
            return self._send(_ok(list(CONNECTIONS.values())))
        return self._send(_err("not found", 40401))

    def do_POST(self):
        path = urlparse(self.path).path
        body = self._read_body()
        if path == "/api/v1/demands":
            return self._create_demand(body)
        if path == "/api/v1/supplies":
            return self._create_supply(body)
        if path == "/api/v1/connections":
            return self._create_connection(body)
        return self._send(_err("not found", 40401))

    def _match(self, demand_id):
        d = DEMANDS.get(demand_id)
        if not d:
            return self._send(_err("demand not found", 40401))
        return self._send(_ok(matching.match(d, list(SUPPLIES.values()))))

    def _create_demand(self, body):
        did = body.get("id") or ("D" + uuid.uuid4().hex[:6])
        d = {
            "id": did, "buyerId": body.get("buyerId", ""),
            "product": body.get("product", ""), "components": body.get("components", {}),
            "quantity": body.get("quantity", 1), "deliveryAddress": body.get("deliveryAddress", ""),
            "budget": body.get("budget", 0), "deadline": body.get("deadline", ""),
        }
        DEMANDS[did] = d
        return self._send(_ok(d))

    def _create_supply(self, body):
        sid = body.get("id") or ("S" + uuid.uuid4().hex[:6])
        s = {
            "id": sid, "supplierId": body.get("supplierId", ""), "category": body.get("category", ""),
            "specs": body.get("specs", ""), "origin": body.get("origin", ""),
            "price": body.get("price", 0), "moq": body.get("moq", 0),
            "stock": body.get("stock", 0), "leadTime": body.get("leadTime", 0),
        }
        SUPPLIES[sid] = s
        return self._send(_ok(s))

    def _create_connection(self, body):
        demand_id = body.get("demandId")
        supply_ids = body.get("supplyIds", [])
        if demand_id not in DEMANDS:
            return self._send(_err("demand not found", 40401))
        missing = [s for s in supply_ids if s not in SUPPLIES]
        if missing:
            return self._send(_err("supplies not found: " + ",".join(missing), 40401))
        cid = "C" + uuid.uuid4().hex[:6]
        c = {"id": cid, "demandId": demand_id, "supplyIds": supply_ids, "status": "connected"}
        CONNECTIONS[cid] = c
        return self._send(_ok(c))

    def log_message(self, *args):
        pass  # 静默日志


def run_demo():
    _load_samples()
    d = DEMANDS.get("D001")
    res = matching.match(d, list(SUPPLIES.values()))
    print("=" * 64)
    print("需求：", d["product"], "x", d["quantity"], " 预算", d["budget"], " 交期", d["deadline"])
    print("推荐组合（每类最优）:", res["recommendedGroup"])
    print("-" * 64)
    for cat, ms in res["matches_by_category"].items():
        print("[" + cat + "]")
        for m in ms:
            s = m["supply"]
            print("  %s(%s) 得分=%s 单价=%s 交期=%s天 MOQ=%s" % (s["supplierId"], s["id"], m["score"], s["price"], s["leadTime"], s["moq"]))
            print("    维度=" + json.dumps(m["dimensions"], ensure_ascii=False) + " 理由=" + json.dumps(m["reasons"], ensure_ascii=False))
    print("-" * 64)
    pick = ["S001", "S002", "S005"]  # a(主板), b(显卡), e(内存)
    print("甲勾选供应：a(S001 主板), b(S002 显卡), e(S005 内存)")
    c = {"id": "C001", "demandId": "D001", "supplyIds": pick, "status": "connected"}
    print("生成意向单:", json.dumps(c, ensure_ascii=False))
    print("=" * 64)


def main():
    _load_samples()
    port = 8000
    print("Outsea backend running at http://127.0.0.1:%d" % port, flush=True)
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()


if __name__ == "__main__":
    if "--demo" in sys.argv:
        run_demo()
    else:
        main()
