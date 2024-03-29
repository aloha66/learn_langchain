# 设置OpenAI API的密钥
import os

import sys

# 将项目的根目录添加到 Python 解释器的路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from util.util import base_url

# 导入库
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# 初始化模型和工具
llm = ChatOpenAI(temperature=0.0, base_url=base_url)
tools = load_tools(
    ["arxiv"],
)

# 初始化链
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# 运行链
# 调invoke后半段报错
agent_chain.run("介绍一下2005.14165这篇论文的创新点?")
