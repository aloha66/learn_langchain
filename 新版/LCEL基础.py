from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

from langchain.globals import set_debug, set_verbose

# set_verbose(True) # 没有更多的信息
set_debug(True)  # 全部的信息，太多了

prompt = PromptTemplate.from_template("{flower}的花语是？")
llm = ChatOpenAI()
output_parser = StrOutputParser()

# 管道
chain = prompt | llm | output_parser
result = chain.invoke({"flower": "玫瑰"})

print(result)
