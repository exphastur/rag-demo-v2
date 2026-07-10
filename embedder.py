"""
embedder.py —— Embedding 封装

为什么单独封装：
  1. embedding 模型加载慢（几秒），不能每次检索都重新加载
  2. 全局只需要一个实例（单例模式），到处 import 同一个对象
  3. 将来换 embedding 模型，只改这一个文件

设计：
  - 模块第一次被 import 时，自动加载模型并缓存
  - 其他模块 `from embedder import embed` 直接用
"""
from sentence_transformers import SentenceTransformer
import config

print(f"[embedder] 正在加载模型 {config.EMBEDDING_MODEL}...")
_model = SentenceTransformer(config.EMBEDDING_MODEL)
print("[embedder] 模型加载完成")


def embed(text: str | list[str]) -> list[list[float]]:
    """
    把文本转成向量。

    输入：
      - 单个字符串：返回 [[向量]]（外层列表长度=1）
      - 字符串列表：返回 [[向量1], [向量2], ...]

    输出：
      嵌套列表，外层=文本数量，内层=向量维度（512维）
    """
    # SentenceTransformer.encode 要求输入是列表
    if isinstance(text, str):
        text = [text]

    return _model.encode(text).tolist()
