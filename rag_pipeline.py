"""
rag_pipeline.py —— RAG 主流程

把检索、Prompt 构造、LLM 调用串成完整的 RAG 流程。

Agent 伏笔：
  ② 决策与执行分层 - 将来 LLM 自己决定要不要检索
  ③ 预留 history 参数 - 将来支持多轮对话
"""
from tools.retriever import retrieve
from prompt import build_prompt
from llm import ask_llm


def answer(question: str, history: list = None, top_k: int = 3) -> str:
    """
    给一个问题，跑完整条 RAG 链路，返回答案。

    参数：
      question: 用户的问题
      history: 对话历史（Agent 伏笔③，当前传 None 占位）
      top_k: 检索返回多少个块（默认 3）

    返回：
      大模型的回答
    """
    # ── 你的任务：把 RAG 的三步串起来 ─────────────────────────
    # 参考 v1 的 query_rag.py 第 39-74 行，但现在每一步都是独立的函数调用
    #
    # 第一步：检索相关资料
    #   调用 retrieve(question, top_k) → 返回 chunks（字符串列表）
    #
    # 第二步：构造 prompt
    #   调用 build_prompt(chunks, question, history) → 返回 prompt（字符串）
    #
    # 第三步：调用 LLM 生成答案
    #   调用 ask_llm(prompt) → 返回 answer（字符串）
    #
    # 最后：return answer

    # TODO：你来写这三步
    chunks = retrieve(question, top_k)
    prompt = build_prompt(chunks, question, history)
    answer = ask_llm(prompt)
    return answer


# ══════════════════════════════════════════════════════════════
# 测试代码
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    test_question = "什么是过拟合？"

    print(f"问题：{test_question}")
    print("=" * 60)
    print("正在检索资料...")

    answer_text = answer(test_question)

    print("\n回答：")
    print(answer_text)
