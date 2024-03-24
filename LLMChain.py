# 使用链
# 导入所需的库
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# 原始字符串模板
template = "{flower}的花语是?"
# 创建模型实例
llm = ChatOpenAI(
    temperature=0,
    base_url="https://api.chatanywhere.tech/v1",
)
# 创建LLMChain
llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(template))
# 调用LLMChain，返回结果
result = llm_chain.invoke("玫瑰")
print(result)


# # 不用链的情况
# # ----第一步 创建提示
# # 导入LangChain中的提示模板
# from langchain.prompts import PromptTemplate

# # 原始字符串模板
# template = "{flower}的花语是?"
# # 创建LangChain模板
# prompt_temp = PromptTemplate.from_template(template)
# # 根据模板创建提示
# prompt = prompt_temp.format(flower="玫瑰")
# # 打印提示的内容
# print(prompt)

# # ----第二步 创建并调用模型
# # 导入LangChain中的OpenAI模型接口
# from langchain_openai import ChatOpenAI

# # 创建模型实例
# llm = ChatOpenAI(
#     temperature=0,
#     base_url="https://api.chatanywhere.tech/v1",
# )
# # 传入提示，调用模型，返回结果
# result = llm.invoke(prompt)
# print(result)
