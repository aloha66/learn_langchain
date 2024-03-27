# 这种方法不适合记住遥远的互动，但它非常擅长限制使用的 Token 数量
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from util import base_url

# 创建大语言模型实例
llm = ChatOpenAI(temperature=0.5, base_url=base_url)

# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationBufferWindowMemory(k=1))

# 第一天的对话
# 回合1
result = conversation.invoke("我姐姐明天要过生日，我需要一束生日花束。")
print(result)
# 回合2
result = conversation.invoke("她喜欢粉色玫瑰，颜色是粉色的。")
# print("\n第二次对话后的记忆:\n", conversation.memory.buffer)
print(result)

# 第二天的对话
# 回合3
result = conversation.invoke("我又来了，还记得我昨天为什么要来买花吗？")
print(result)
