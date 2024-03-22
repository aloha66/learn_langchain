from langchain.prompts import PromptTemplate

# 方式一 from_template
template = """\
你是业务咨询顾问。
你给一个销售{product}的电商公司，起一个好的名字？
"""
prompt = PromptTemplate.from_template(template)

print(prompt.format(product="鲜花"))

# 方式二 构造函数
prompt = PromptTemplate(
    input_variables=["product", "market"],
    template="你是业务咨询顾问。对于一个面向{market}市场的，专注于销售{product}的公司，你会推荐哪个名字？",
)
print(prompt.format(product="鲜花", market="高端"))


# 聊天模型

# 导入聊天消息类模板
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 模板的构建
template = "你是一位专业顾问，负责为专注于{product}的公司起名。"
system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "公司主打产品是{product_detail}。"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
prompt_template = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

# 格式化提示消息生成提示
prompt = prompt_template.format_prompt(
    product="鲜花装饰", product_detail="创新的鲜花设计。"
).to_messages()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.chatanywhere.tech/v1",
)
result = llm.invoke(prompt)
print(result)
