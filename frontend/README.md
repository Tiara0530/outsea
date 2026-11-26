# frontend/ —— 成员2 · 前端工程师

> 你的职责：做界面、接 API，做出可演示的 Web 应用。

## 我的工作（一句话）
用 React + Vite + TypeScript 做首页 + 三个功能页（商品本地化 / 跨文化沟通 / 出海情报），按接口规范调用后端。

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
    ├── api/           # 封装后端接口调用
    ├── pages/         # 首页 + 三个功能页
    └── components/
```

## 依赖与被依赖
- **依赖**：成员1 的接口规范（可先用 mock 数据并行开发）。
- **被依赖**：成员5 需要我可演示的版本录 Demo。

## 验收标准
- [ ] 应用可本地启动，页面完整。
- [ ] 三个功能都能输入并展示结果（先 mock，后接真接口）。
- [ ] 接口异常有友好提示。

## 我的任务清单
- [ ] 搭建 Vite + React + TS 骨架
- [ ] 首页 + 导航布局
- [ ] 商品本地化页（mock）
- [ ] 跨文化沟通页（mock）
- [ ] 出海情报页（mock）
- [ ] 封装 api 层，接真实后端接口
- [ ] 打磨 UI 与交互（配合录 Demo）

## 怎么开始
```bash
cd frontend
npm install
npm run dev
```
先把三个页面和 mock 交互搭出来，后端接口好了再切换到真实调用。
