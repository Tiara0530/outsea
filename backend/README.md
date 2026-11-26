# backend/ —— 成员1 · 组长 · 后端架构与编排

> 你的职责：定架构、出接口、写后端、把前端/引擎/数据串起来。

## 我的工作（一句话）
我是唯一对外入口，写 FastAPI 后端，把成员2（前端）的请求编排给成员3（引擎）和成员4（数据），再汇总返回。

## 目录结构（建议）
```
backend/
├── README.md
├── requirements.txt        # 依赖
├── app/
│   ├── main.py             # 入口 + 路由
│   ├── routes/             # localize / communicate / intel
│   ├── services/           # 调用 ai-engine、data-pipeline
│   └── schema/             # 请求/响应模型
└── tests/
```

## 依赖与被依赖
- **依赖**：无（我第一个出接口规范）。
- **被依赖**：成员2/3/4 都按我定的 `docs/03-接口规范.md` 对接。

## 验收标准（做完就算我过关）
- [ ] `GET /api/v1/health` 可访问。
- [ ] `localize` / `communicate` / `intel/search` 三个接口先用 mock 跑通。
- [ ] 统一响应格式 + 错误码按规范实现。
- [ ] 联调后三功能真实串联引擎/数据。

## 我的任务清单
- [ ] 定稿技术栈与目录结构
- [ ] 定稿并同步 `docs/03-接口规范.md`
- [ ] 搭建 FastAPI 骨架 + health 接口
- [ ] 实现三个接口的 mock 版本
- [ ] 对接成员3 的 ai-engine
- [ ] 对接成员4 的 data-pipeline
- [ ] 端到端联调收口

## 怎么开始
```bash
cd backend
python -m venv .venv && .venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```
先跑通 health，再补三个 mock 接口。
