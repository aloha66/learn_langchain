from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from langchain_core.output_parsers import StrOutputParser

from langchain.globals import set_debug, set_verbose

import os

# 添加两个环境变量就可以追踪整个链路了
# os.environ["LANGCHAIN_TRACING_V2"] = "True"
# os.environ["LANGCHAIN_API_KEY"] = ""


# set_verbose(True) # 没有更多的信息
# set_debug(True)  # 全部的信息，太多了

prompt = PromptTemplate.from_template("{flower}的花语是？")
llm = ChatOpenAI()
output_parser = StrOutputParser()

# 管道
chain = prompt | llm | output_parser
result = chain.invoke({"flower": "雏菊"})

print(result)
