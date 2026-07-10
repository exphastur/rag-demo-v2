"""
build_rag.py —— 建库脚本（只需要运行一次）

流程：
  原始文档 → 切块 → embedding → 存入向量库

和 v1 的区别：
  - 配置从 config.py 统一读取
  - embedder 从独立模块 import
  - 向量库初始化逻辑也可以复用，为将来多文档建库做准备
"""
import config
from embedder import embed
import chromadb

# ══════════════════════════════════════════════════════════════
# 测试文档（和 v1 一样）
# ══════════════════════════════════════════════════════════════
DOCUMENT = """
机器学习是人工智能的一个分支,核心思想是让计算机从数据中自动学习规律,而不是由人手写死规则。
监督学习使用带标签的数据训练模型,比如给一堆标好"猫/狗"的图片让模型学会分辨。
无监督学习处理没有标签的数据,典型任务是聚类,把相似的数据自动分成几组。
过拟合指模型在训练数据上表现很好,但在没见过的新数据上表现很差,通常是因为模型把训练数据的噪声也背了下来。
深度学习是机器学习的一个子领域,使用多层神经网络,在图像、语音、自然语言处理上取得了突破性进展。
Transformer 是一种基于注意力机制的神经网络架构,是现代大语言模型的基础。
""".strip()


# ══════════════════════════════════════════════════════════════
# 切块函数（和 v1 一样，你写的）
# ══════════════════════════════════════════════════════════════
def chunk_text(text: str) -> list[str]:
    """
    按行切块。

    为什么按行切：
      上面的文档每行正好是一个完整的知识点。
      真实项目里，切块策略要根据文档结构调整（段落、句子、固定长度等）。

    输入：一大段文本
    输出：字符串列表，每个元素是一个块
    """
    return [line for line in text.splitlines() if line.strip()]


# ══════════════════════════════════════════════════════════════
# 主流程：切块 → embedding → 存储
# ══════════════════════════════════════════════════════════════
def main():
    print("=" * 60)
    print("开始建库")
    print("=" * 60)

    # 1. 切块
    chunks = chunk_text(DOCUMENT)
    print(f"\n[1/3] 切块完成：共 {len(chunks)} 块")

    # 2. 转向量
    embeddings = embed(chunks)
    print(f"[2/3] 向量化完成：每块向量维度 {len(embeddings[0])}")

    # 3. 存入 Chroma
    client = chromadb.PersistentClient(path=config.CHROMA_DB_PATH)
    collection = client.get_or_create_collection(config.COLLECTION_NAME)

    collection.upsert(
        ids=[f"chunk-{i}" for i in range(len(chunks))],
        embeddings=embeddings,
        documents=chunks,
    )
    print(f"[3/3] 存储完成：{len(chunks)} 个块已写入 {config.CHROMA_DB_PATH}")

    print("\n" + "=" * 60)
    print("建库完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
