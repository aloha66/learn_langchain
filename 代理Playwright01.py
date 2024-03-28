# 有点尴尬 initialize_agent是废弃api，官网给出的例子是不使用STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
# 第二个尴尬点是 他知道我这是一个网站但获取不了数据
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from langchain_community.tools.playwright.utils import create_async_playwright_browser
from util import base_url

async_browser = create_async_playwright_browser()
toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = toolkit.get_tools()
print(tools)

from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI

# LLM不稳定，对于这个任务，可能要多跑几次才能得到正确结果
llm = ChatOpenAI(temperature=0.5, base_url=base_url)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


async def main():
    response = await agent_chain.arun("What are the headers on python.langchain.com?")
    print(response)


import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
