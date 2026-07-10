"""
config.py —— 所有配置集中管理

为什么要有这个文件：
  - 避免魔法字符串散落在各处（模型名、路径改一次要改十个文件）
  - 环境变量、路径、模型名全在这，一眼看清整个项目的依赖
"""
import os
from dotenv import load_dotenv

# 读取项目根目录的 .env 文件，把里面的键值对加载进环境变量
# （.env 不提交 Git，敏感信息只存在本地）
load_dotenv()

# ══════════════════════════════════════════════════════════════
# LLM 配置（中转站）—— 敏感信息全部走环境变量，不硬编码
# ══════════════════════════════════════════════════════════════
LLM_BASE_URL = os.environ.get("MODELGATE_BASE_URL")
LLM_MODEL = "DeepSeek-V4-Flash"  # 便宜、快，适合 RAG 内部调用
LLM_API_KEY = os.environ.get("MODELGATE_API_KEY")

if not LLM_BASE_URL:
    raise ValueError("环境变量 MODELGATE_BASE_URL 未设置（请在 .env 中配置）")
if not LLM_API_KEY:
    raise ValueError("环境变量 MODELGATE_API_KEY 未设置（请在 .env 中配置）")

# ══════════════════════════════════════════════════════════════
# Embedding 配置（本地）
# ══════════════════════════════════════════════════════════════
EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"  # 中文、免费、离线

# 强制离线模式：避免每次启动检查 HuggingFace 在线更新
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

# ══════════════════════════════════════════════════════════════
# 向量库配置
# ══════════════════════════════════════════════════════════════
CHROMA_DB_PATH = "./chroma_db"
COLLECTION_NAME = "rag_v2_collection"

# ══════════════════════════════════════════════════════════════
# RAG 检索参数
# ══════════════════════════════════════════════════════════════
DEFAULT_TOP_K = 3  # 默认检索返回多少个块
