"""
llm.py —— 大模型调用

把 prompt 喂给 OpenAI API，拿回答案。
"""
import config
from openai import OpenAI


# ══════════════════════════════════════════════════════════════
# 初始化 OpenAI 客户端（模块加载时执行一次）
# ══════════════════════════════════════════════════════════════
# TODO：你来写
# 提示：
#   1. 创建 OpenAI 客户端：client = OpenAI(api_key=config.OPENAI_API_KEY)
#   2. 如果你用的是其他兼容 OpenAI 的服务（如 deepseek），需要额外传 base_url 参数
# 参考 v1 的 query_rag.py 第 26 行

_client = OpenAI(api_key=config.LLM_API_KEY, base_url=config.LLM_BASE_URL)



# ══════════════════════════════════════════════════════════════
# 核心函数：调用大模型
# ══════════════════════════════════════════════════════════════
def ask_llm(prompt: str) -> str:
    """
    把 prompt 发给大模型，返回回答。

    参数：
      prompt: 完整的 prompt 字符串（从 prompt.py 的 build_prompt 返回的）

    返回：
      模型的回答（字符串）
    """
    # TODO：你来写
    # 提示：
    #   1. 调用 _client.chat.completions.create(...)
    #   2. 参数：
    #      - model: config.MODEL_NAME
    #      - messages: [{"role": "user", "content": prompt}]
    #   3. 从返回结果里取出回答：response.choices[0].message.content
    # 参考 v1 的 query_rag.py 第 86-91 行

    # 第一步：调用 API
    # response = _client.chat.completions.create(...)

    # 第二步：提取回答
    # answer = response.choices[0].message.content

    # return answer
    llmres =_client.chat.completions.create(messages= [{"role" : 'user', "content" : prompt}],model=config.LLM_MODEL)

    answer = llmres.choices[0].message.content
    return answer


# ══════════════════════════════════════════════════════════════
# 测试代码
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    test_prompt = "请用一句话解释什么是机器学习。"

    print("测试 LLM 调用...")
    answer = ask_llm(test_prompt)
    print("=" * 60)
    print("回答：")
    print(answer)
