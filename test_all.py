"""快速测试 - 不需要交互输入"""
from rag_pipeline import answer

questions = [
    "什么是过拟合？",
    "什么是Transformer？",
    "什么是机器学习？"
]

for q in questions:
    print(f"\n{'='*60}")
    print(f"问题：{q}")
    print('='*60)
    result = answer(q)
    print(f"回答：{result}")
