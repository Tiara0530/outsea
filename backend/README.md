# backend/ —— 成员1 · 组长 · 后端

> 职责：定架构、供需数据模型、API、匹配编排、连接（意向单）。

## 我的工作（一句话）
我是唯一对外入口，写 FastAPI 后端：发布需求、上架供给、调用匹配引擎做编排、建立连接（意向单）。

## 目录结构（建议）
```
backend/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py            # 入口 + 路由
│   ├── models/            # Demand / Supply / Connection
│   ├── routes/            # demands / supplies / match / connections
│   └── services/          # 调用 ai-engine、data-pipeline
└── tests/
```

## 依赖与被依赖
- 依赖：无（我先出接口规范）。
- 被依赖：成员2/3/4 都按我定的 `docs/03-接口规范.md` 对接。

## 验收标准
- [ ] 发布需求、上架供给、匹配、建立连接 四个接口可用。
- [ ] 统一响应格式 + 错误码按规范实现。
- [ ] 前后端/引擎/数据真实串联，全流程跑通。

## 任务清单
- [ ] 定稿架构与 `docs/03-接口规范.md`
- [ ] 搭建 FastAPI 骨架 + health
- [ ] 实现四个接口 mock 版本
- [ ] 对接成员3 的匹配引擎
- [ ] 对接成员4 的数据服务
- [ ] 端到端联调收口

## 怎么开始
```bash
cd backend
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
先跑通 health，再补四个接口 mock。
