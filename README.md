# RAG v2 - 知识库问答系统

> 从零实现的 RAG（Retrieval-Augmented Generation）系统，支持本地知识库检索 + 大模型生成回答。

---

## 项目简介

从零开始实现RAG 实现优先查阅本地文档回答问题

---

## 技术栈


- Python 3.11
- sentence-transformers（本地 embedding）
- chromadb（向量数据库）
- OpenAI API（LLM 调用）


---

## 核心功能


- 本地 embedding，不依赖在线 API
- 向量检索，语义匹配相关资料
- 将本地文档切块向量化
- 整合提示词调用llm
- 流水线式链式调度

---

## 项目结构



```
rag-demo-v2/
├── config.py          # 配置中心
├── embedder.py        # Embedding 封装
├── tools/
│   └── retriever.py   # 检索工具
├── prompt.py          # Prompt 构造
├── llm.py             # LLM 调用
├── rag_pipeline.py    # 主流程
├── build_rag.py       # 建库脚本
├── main.py            # 入口
└── README.md
```

---

## 快速开始


  # 1. 安装依赖
  pip install -r requirements.txt

  # 2. 设置环境变量
  export MODELGATE_API_KEY="your_key"

  # 3. 建库
  python build_rag.py

  # 4. 运行
  python main.py

---

## Agent 伏笔

本项目在架构设计时预留了升级为 Agent 的扩展点：

1. **检索抽象成 tool**（`tools/retriever.py`）  
   将检索封装成独立函数 `retrieve(query) -> chunks`，将来 Agent 框架可以直接注册为工具，无需修改内部逻辑。

2. **决策与执行分层**（`rag_pipeline.py`）  
   当前版本必然检索一次，但架构上已经分离了"决定要检索"和"执行检索"两个步骤，将来可升级为 ReAct 循环（LLM 自己决定是否检索、检索什么）。

3. **预留 history 参数**  
   所有核心函数（`build_prompt`、`answer`）都预留了 `history` 参数占位，将来可直接扩展为多轮对话和记忆模块。

---

## 下一步计划

- [ ] 替换测试文档为真实资料
- [ ] 实现多轮对话（利用预留的 history 参数）
- [ ] 优化检索质量（调整切块策略、hybrid search、reranking）
- [ ] 升级为 Agent 系统（ReAct 循环、多工具调用、规划能力）

---

## 作者

【Grx / GitHub】
