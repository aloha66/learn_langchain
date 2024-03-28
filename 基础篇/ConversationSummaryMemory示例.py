# 这种方法存在翻译的误差，把姐姐回答成妹妹了
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory
import os
import sys

# 将项目的根目录添加到 Python 解释器的路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from util.util import base_url


# 创建大语言模型实例
llm = ChatOpenAI(temperature=0.5, base_url=base_url)


# 初始化对话链
conversation = ConversationChain(llm=llm, memory=ConversationSummaryMemory(llm=llm))


# 第一天的对话
# 回合1
result = conversation.invoke("我姐姐明天要过生日，我需要一束生日花束。")
print("回合1", result)
# 回合2
result = conversation.invoke("她喜欢粉色玫瑰，颜色是粉色的。")
# print("\n第二次对话后的记忆:\n", conversation.memory.buffer)
print("回合2", result)

# 第二天的对话
# 回合3
result = conversation.invoke("我又来了，还记得我昨天为什么要来买花吗？")
print("回合3", result)
