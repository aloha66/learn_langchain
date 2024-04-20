# 导入所需的库和模块
from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI


# 创建一个聊天模型的实例
chat = ChatOpenAI()

# 创建一个消息列表
messages = [
    SystemMessage(content="你是一个花卉行家。"),
    HumanMessage(content="朋友喜欢淡雅的颜色，她的婚礼我选择什么花？"),
]

# 使用聊天模型获取响应
response = chat.invoke(messages)
print(response)
