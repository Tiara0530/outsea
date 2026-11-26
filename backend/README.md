# backend/ —— 成员1 · 组长 · 后端

> 职责：定架构、供需数据模型、API、匹配编排、连接（意向单）。

## 我的工作（一句话）
我是唯一对外入口，实现需求发布、供给上架、匹配编排、建立连接（意向单）四个核心能力。

## 目录结构（初始版已落地）
```
backend/
├── README.md
├── main.py            # HTTP 接口 + 编排（8 个接口）
├── matching.py        # 匹配引擎（兼容性硬门槛 + 成本/利润/效率打分）
├── data.py            # 演示数据（甲 + a,b,c,d,e 及竞品）
└── requirements.txt   # 初始版零依赖，Python 3 即可
```

## 运行方式（零依赖）
```bash
cd backend
python main.py --demo    # 演示完整匹配流程
python main.py           # 启动服务 http://127.0.0.1:8000
```

## 接口清单（详见 docs/03-接口规范.md）
`health` · `demands`(GET/POST) · `supplies`(GET/POST) · `match/{id}` · `connections`(GET/POST)

## 验收标准
- [ ] 发布需求、上架供给、匹配、建立连接 四个核心能力可用。
- [ ] 匹配推荐「甲 → a,b,c,d,e」正确，不兼容者被排除。
- [ ] 统一响应格式 + 错误码按规范实现。
- [ ] 前后端/引擎/数据真实串联，全流程跑通。

## 任务清单
- [x] 定稿 `docs/03-接口规范.md`
- [x] 数据模型 + 样例数据
- [x] 匹配引擎（兼容性硬门槛 + 三维打分）
- [x] 八个 HTTP 接口
- [ ] 对接成员2 前端（后续）
- [ ] 端到端联调收口

## 怎么开始
直接 `python main.py --demo` 先看演示，再 `python main.py` 起服务联调。
