# 显式地指定索引创建器的 vectorstore、embedding 以及 text_splitter
from langchain.text_splitter import CharacterTextSplitter

# 使用VectorstoreIndexCreator来从加载器创建索引
from langchain.indexes import VectorstoreIndexCreator

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

index_creator = VectorstoreIndexCreator(
    vectorstore_cls=Chroma,
    embedding=OpenAIEmbeddings(),
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0),
)


# 导入文档加载器模块，并使用TextLoader来加载文本文件
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./OneFlower/花语大全.txt", encoding="utf8")

index = index_creator.from_loaders([loader])


from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

# 定义查询字符串, 使用创建的索引执行查询
query = "玫瑰花的花语是什么？"
# llm也不是必须，因为base_url的源不支持他默认的模型，所以也要覆盖他
result = index.query(query, llm=llm)
print(result)  # 打印查询结果
