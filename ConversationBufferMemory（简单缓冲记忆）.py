from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from util import base_url

# 初始化大语言模型
llm = ChatOpenAI(temperature=0.5, base_url=base_url)

# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

# 第一天的对话
# 回合1
conversation.invoke("我姐姐明天要过生日，我需要一束生日花束。")
print("第一次对话后的记忆:", conversation.memory.buffer)

# 回合2
conversation.invoke("她喜欢粉色玫瑰，颜色是粉色的。")
print("第二次对话后的记忆:", conversation.memory.buffer)

# 回合3 （第二天的对话）
conversation.invoke("我又来了，还记得我昨天为什么要来买花吗？")
print("/n第三次对话后时提示:/n", conversation.prompt.template)
print("/n第三次对话后的记忆:/n", conversation.memory.buffer)
