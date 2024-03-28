# 使用 LCEL 构建的链,代替路由链
# 目前会抛这个waring,但是不影响使用
# UserWarning: The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain

# 路由链的内部策略
# EmbeddingRouterChain使用输入的嵌入向量与目标链描述的嵌入向量进行相似性比较,
# 选择相似度最高的链。LLMRouterChain使用小型语言模型根据目标链的描述来选择链。
# RouterChain自动处理路由逻辑,用户只需要提供目标链,而不需要编写选择目标链的提示。
# 它动态地根据每个输入选择下一个链,实现了可配置的多任务链

# 1. 构建两个场景的模板
flower_care_template = """你是一个经验丰富的园丁，擅长解答关于养花育花的问题。
                        下面是需要你来回答的问题:
                        {input}"""

flower_deco_template = """你是一位网红插花大师，擅长解答关于鲜花装饰的问题。
                        下面是需要你来回答的问题:
                        {input}"""

# 2. 构建提示信息
prompt_infos = [
    {
        "key": "flower_care",
        "description": "适合回答关于鲜花护理的问题",
        "template": flower_care_template,
    },
    {
        "key": "flower_decoration",
        "description": "适合回答关于鲜花装饰的问题",
        "template": flower_deco_template,
    },
]

prompt_infos2 = [
    {
        "name": "flower_care",
        "description": "适合回答关于鲜花护理的问题",
        "prompt_template": flower_care_template,
    },
    {
        "name": "flower_decoration",
        "description": "适合回答关于鲜花装饰的问题",
        "prompt_template": flower_deco_template,
    },
]

# 3. 初始化语言模型
from langchain_openai import ChatOpenAI
import os
import sys

# 将项目的根目录添加到 Python 解释器的路径中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from util.util import base_url

llm = ChatOpenAI(base_url=base_url)


# 4. 构建目标链
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

chain_map = {}
for info in prompt_infos:
    prompt = PromptTemplate(template=info["template"], input_variables=["input"])
    print("目标提示:\n", prompt)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    chain_map[info["key"]] = chain

# 5. 构建路由链
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import (
    MULTI_PROMPT_ROUTER_TEMPLATE as RounterTemplate,
)

destinations = [f"{p['key']}: {p['description']}" for p in prompt_infos]
router_template = RounterTemplate.format(destinations="\n".join(destinations))
print("路由模板:\n", router_template)
router_prompt = PromptTemplate(
    template=router_template,
    input_variables=["input"],
    output_parser=RouterOutputParser(),
)
print("路由提示:\n", router_prompt)
router_chain = LLMRouterChain.from_llm(llm, router_prompt, verbose=True)


# 6. 构建默认链
from langchain.chains import ConversationChain

default_chain = ConversationChain(llm=llm, output_key="text", verbose=True)


# 7. 构建多提示链
from langchain.chains.router import MultiPromptChain

# 提供两种方式构建路由链
# chain = MultiPromptChain(
#     router_chain=router_chain,
#     destination_chains=chain_map,
#     default_chain=default_chain,
#     verbose=True,
# )

chain = MultiPromptChain.from_prompts(llm=llm, prompt_infos=prompt_infos2, verbose=True)

# 8. 测试
# 三个方向
print(chain.invoke("如何为玫瑰浇水"))
# print(chain.invoke("如何为婚礼场地装饰花朵？"))
# print(chain.invoke("如何考入哈佛大学？"))
