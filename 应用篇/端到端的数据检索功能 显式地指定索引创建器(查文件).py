# 导入文档加载器模块，并使用TextLoader来加载文本文件
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./OneFlower/花语大全.txt", encoding="utf8")

# 使用VectorstoreIndexCreator来从加载器创建索引
from langchain.indexes import VectorstoreIndexCreator

from langchain_openai import OpenAIEmbeddings

embedding = OpenAIEmbeddings()
# embedding不是必须，他默认的embedding是旧版本的引用（抛了一个warning）
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

# 定义查询字符串, 使用创建的索引执行查询
query = "玫瑰花的花语是什么？"
# llm也不是必须，因为base_url的源不支持他默认的模型，所以也要覆盖他
result = index.query(query, llm=llm)
print(result)  # 打印查询结果
