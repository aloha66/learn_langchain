from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from util import base_url

# 初始化大语言模型
llm = ChatOpenAI(temperature=0.5, base_url=base_url)

# 初始化对话链
conv_chain = ConversationChain(llm=llm)

# 打印对话的模板
print(conv_chain.prompt.template)
