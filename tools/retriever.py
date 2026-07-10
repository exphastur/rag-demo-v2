"""
retriever.py —— 检索工具

这是 RAG 系统的"检索引擎"，也是 Agent 伏笔的第①条关键。

为什么要单独封装：
  - Agent 的本质是"调用工具"：思考 → 决定调哪个工具 → 调用 → 拿结果 → 继续思考
  - 把检索抽象成一个 retrieve(query) -> chunks 的函数，将来升级成 Agent 时，
    只需要把这个函数注册到 Agent 的工具列表里，不需要改任何内部逻辑
  - 如果检索和回答混在一起（v1 的 answer()），Agent 框架没法单独调"只检索"

设计原则：
  - 输入：自然语言问题（字符串）
  - 输出：相关文本块（字符串列表）
  - 不关心谁调用、为什么调用、拿结果干什么
"""
import chromadb
import config
import embedder
from embedder import embed


# ══════════════════════════════════════════════════════════════
# 初始化向量库连接（模块加载时执行一次，不是每次调用都重新连）
# ══════════════════════════════════════════════════════════════
# TODO：你来写
# 提示：需要初始化 chromadb 的 client 和 collection
# 参考 v1 的 query_rag.py 第 29-30 行

_client = chromadb.PersistentClient(path=config.CHROMA_DB_PATH)
_collection = _client.get_collection(config.COLLECTION_NAME)


# ══════════════════════════════════════════════════════════════
# 核心函数：检索工具
# ══════════════════════════════════════════════════════════════
def retrieve(query: str, top_k: int = config.DEFAULT_TOP_K) -> list[str]:
    """
    给一个问题，从向量库里找最相关的 top_k 个文本块。

    这是一个"纯工具函数"：
      输入 → 处理 → 输出，不依赖外部状态（除了向量库），不产生副作用。

    参数：
      query: 用户的问题（自然语言）
      top_k: 返回多少个最相关的块（默认从 config 读取）

    返回：
      字符串列表，每个元素是一块原始文本

    Agent 升级时的用法（未来）：
      agent.register_tool(
          name="retrieve",
          description="从知识库检索相关资料",
          function=retrieve
      )
    """
    # TODO：你来写检索逻辑
    # 提示：分两步
    #   1. 把 query 转成向量（用 embedder.embed）
    #   2. 调用 _collection.query 找最近的 top_k 个块
    # 参考 v1 的 query_rag.py 第 44-48 行

    # 第一步：问题 → 向量
    query_vector = embed(query)  # embed() 返回 [[向量]]，已经是列表套列表

    # 第二步：向量 → 检索最近的块
    hits = _collection.query(query_embeddings=query_vector, n_results=top_k)
    chunks = hits["documents"][0]  # 注意是 "documents" 复数

    return chunks
    print(f"检索到{len(chunks)}个相关快")
    for i, c in enumerate(chunks):
        print(f"[{i+1}] {c}")

    return chunks


# ══════════════════════════════════════════════════════════════
# 测试代码（可选，方便你单独测试这个模块）
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # 确保先运行过 build_rag.py 建库
    test_query = "什么是过拟合？"
    print(f"测试查询: {test_query}")
    print("=" * 60)

    results = retrieve(test_query)

    print(f"\n检索到 {len(results)} 个相关块:")
    for i, chunk in enumerate(results, 1):
        print(f"[{i}] {chunk}")
