# 官网代码也是高概率报错
# 导入langchain的实用工具和相关的模块
from langchain_community.utilities import SQLDatabase

from langchain_openai import ChatOpenAI

from langchain.chains import create_sql_query_chain


db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")


# 创建OpenAI的低级语言模型（LLM）实例，这里我们设置温度为0，意味着模型输出会更加确定性
llm = ChatOpenAI(temperature=0, verbose=True)
chain = create_sql_query_chain(llm, db)


# 运行与鲜花运营相关的问题
try:
    response = chain.invoke({"question": "有多少种不同的鲜花？"})
    print(111, response)
    print(222, db.run(response))
except Exception as e:
    print(e)

# response = db_chain.invoke("哪种鲜花的存货数量最少？")
# print(response)

# response = db_chain.invoke("平均销售价格是多少？")
# print(response)

# response = db_chain.invoke("从法国进口的鲜花有多少种？")
# print(response)

# response = db_chain.invoke("哪种鲜花的销售量最高？")
# print(response)
