# TODO 这个答案不符合预期，答案不稳定，多试几次有对了
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType

# 连接到FlowerShop数据库
db = SQLDatabase.from_uri("sqlite:///FlowerShop.db")
llm = ChatOpenAI(temperature=0, verbose=True)

# 创建SQL Agent
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

# 使用Agent执行SQL查询

questions = [
    # 这个答案不符合预期'output': 'There are X different types of flowers.'
    "有多少种不同的鲜花？"
    # "哪种鲜花的存货数量最少？",
    # "平均销售价格是多少？",
]

for question in questions:
    response = agent_executor.invoke(question)
    print(response)
