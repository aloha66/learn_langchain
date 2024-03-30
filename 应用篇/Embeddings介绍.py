# 初始化Embedding类
from langchain_openai import OpenAIEmbeddings

# 设置OpenAI API的密钥
import os

import sys

# 将项目的根目录添加到 Python 解释器的路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from util.util import base_url


embeddings_model = OpenAIEmbeddings(base_url=base_url)

# 这个方法接收多个文本作为输入，意味着你可以一次性将多个文档转换为它们的向量表示

# embeddings = embeddings_model.embed_documents(
#     [
#         "您好，有什么需要帮忙的吗？",
#         "哦，你好！昨天我订的花几天送达",
#         "请您提供一些订单号？",
#         "12345678",
#     ]
# )
# print(embeddings)


# len(embeddings), len(embeddings[0])

embedded_query = embeddings_model.embed_query("刚才对话中的订单号是多少?")
print(embedded_query[:3])
