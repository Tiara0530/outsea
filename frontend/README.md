# frontend/ —— 成员2 · 前端

> 职责：需求方端 + 供给方端 + 匹配结果/意向单展示。

## 我的工作（一句话）
用 React + Vite + TypeScript 做两端界面：需求方发需求/看匹配/勾选供应商，供给方上架/管理资源。

## 目录结构（建议）
```
frontend/
├── README.md
├── package.json
├── vite.config.ts
├── index.html
└── src/
    ├── main.tsx
    ├── App.tsx
    ├── api/            # 封装后端接口
    ├── pages/
    │   ├── BuyerHome.tsx    # 需求方：发布需求
    │   ├── MatchResult.tsx  # 匹配结果 + 勾选供应商
    │   ├── SupplierHome.tsx # 供给方：上架资源
    │   └── Connections.tsx  # 意向单
    └── components/
```

## 依赖与被依赖
- 依赖：成员1 接口规范（可先 mock 并行开发）。
- 被依赖：成员5 录 Demo。

## 验收标准
- [ ] 两端页面可操作。
- [ ] 跑通「甲发布需求 → 看到匹配 → 勾选 a,b,e → 生成意向单」全流程。

## 任务清单
- [ ] 搭 Vite + React + TS 骨架
- [ ] 需求方端（发布需求）
- [ ] 匹配结果 + 勾选供应商
- [ ] 供给方端（上架/管理）
- [ ] 意向单展示
- [ ] 封装 api 层，接真实后端
- [ ] 打磨 UI（配合录 Demo）

## 怎么开始
```bash
cd frontend
npm install
npm run dev
```
先用 mock 把「甲→a,b,e」流程界面搭出来，后端好了再切真实调用。
