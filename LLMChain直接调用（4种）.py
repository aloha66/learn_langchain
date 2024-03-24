# 导入所需的库
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain


prompt = PromptTemplate(
    input_variables=["flower", "season"],
    template="{flower}在{season}的花语是?",
)

# 创建模型实例
llm = ChatOpenAI(
    temperature=0,
    base_url="https://api.chatanywhere.tech/v1",
)
# 创建LLMChain
llm_chain = LLMChain(llm=llm, prompt=prompt)
# 4种调用方式
# 调用LLMChain，返回结果
# result = llm_chain.invoke({"flower": "玫瑰", "season": "夏季"})
# 传参方式不同
# result = llm_chain.predict(flower="玫瑰", season="夏季")

# apply允许您针对输入列表运行链
input_list = [
    {"flower": "玫瑰", "season": "夏季"},
    {"flower": "百合", "season": "春季"},
    {"flower": "郁金香", "season": "秋季"},
]
# 返回字符串数组
# result = llm_chain.apply(input_list)

result = llm_chain.generate(input_list)

print(result)
