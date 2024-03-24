# 从langchain库导入所需的模块
from langchain_openai import ChatOpenAI
from langchain.output_parsers import OutputFixingParser


# 导入所需要的库和模块
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


# 使用Pydantic创建一个数据格式，表示花
class Flower(BaseModel):
    name: str = Field(description="name of a flower")
    colors: List[str] = Field(description="the colors of this flower")


# 定义一个用于获取某种花的颜色列表的查询
flower_query = "Generate the charaters for a random flower."

# 定义一个格式不正确的输出
# Python 期望属性名称被双引号包围，但在给定的 JSON 字符串中是单引号
misformatted = "{'name': '康乃馨', 'colors': ['粉红色','白色','红色','紫色','黄色']}"

# # 创建一个用于解析输出的Pydantic解析器，此处希望解析为Flower格式
parser = PydanticOutputParser(pydantic_object=Flower)
# # 使用Pydantic解析器解析不正确的输出
# parser.parse(misformatted)

# 使用OutputFixingParser创建一个新的解析器，该解析器能够纠正格式不正确的输出
new_parser = OutputFixingParser.from_llm(
    parser=parser,
    llm=ChatOpenAI(
        base_url="https://api.chatanywhere.tech/v1",
    ),
)

# 使用新的解析器解析不正确的输出
result = new_parser.parse(misformatted)  # 错误被自动修正
print(result)  # 打印解析后的输出结果
