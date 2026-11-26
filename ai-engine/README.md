# ai-engine/ —— 成员3 · AI/LLM 工程师

> 你的职责：让「本地化 ≠ 翻译」，把 Prompt 和生成引擎做扎实。

## 我的工作（一句话）
负责模型接入 + Prompt 工程，写「商品本地化」和「跨文化沟通」两个生成引擎，输出格式稳定的 JSON。

## 目录结构（建议）
```
ai-engine/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py            # /engine/localize /engine/communicate /engine/health
│   ├── llm.py             # 模型接入（官方 Token 补贴）
│   ├── prompts/           # Prompt 库
│   │   ├── localize.py
│   │   └── communicate.py
│   └── culture_rules/     # 目标市场语气/禁忌规则
└── samples/               # 输入输出示例
```

## 依赖与被依赖
- **依赖**：成员1 的引擎接口约定（`docs/03-接口规范.md` 第 3 节）。
- **被依赖**：成员1 的 backend 调用我；成员2 展示我的输出。

## 验收标准
- [ ] 中文商品信息 → 稳定产出目标语言标题/五点/关键词（JSON）。
- [ ] 中文意图 → 目标市场邮件/客服话术，语气本地化。
- [ ] 输出格式符合接口规范，无脏输出。

## 我的任务清单
- [ ] 选型并接入模型 API（用官方 Token 补贴）
- [ ] 写商品本地化 Prompt + 引擎
- [ ] 写跨文化沟通 Prompt + 引擎
- [ ] 建目标市场文化规则（至少 2 个市场）
- [ ] 保证输出为标准 JSON，容错处理
- [ ] 调优生成质量，准备演示样例

## 怎么开始
先准备 3–5 个「中文输入 → 理想输出」示例（放 `samples/`），再据此写 Prompt，用示例反复调，直到输出稳定。
