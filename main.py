"""
main.py —— RAG v2 入口

运行方式：
  python main.py

交互式问答（可选扩展）：
  while True 循环，持续问答
"""
from rag_pipeline import answer


def main():
    """主函数：单次问答"""
    print("=" * 60)
    print("RAG v2 - 知识库问答系统")
    print("=" * 60)

    # 单次问答
    question = input("\n请输入问题：").strip()  # 去掉首尾空白

    if not question:
        print("问题不能为空")
        return

    print("\n正在检索并生成答案...\n")
    answer_text = answer(question)

    print("回答：")
    print(answer_text)
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
