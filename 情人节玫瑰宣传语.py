import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="https://api.chatanywhere.tech/v1")
text = llm.invoke("请给我写一句情人节红玫瑰的中文宣传语")
print(text)
