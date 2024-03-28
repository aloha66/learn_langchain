from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import ( SystemMessage)

prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个很棒的智能助手"),
    ("user", "{input}")
])

llm = ChatOpenAI(  
    model="gpt-3.5-turbo",
    base_url="https://api.chatanywhere.tech/v1",
    temperature=0.8,
    max_tokens=60,)


chain = prompt | llm
response = chain.invoke({"input":"请给我的花店起个名"})
print(response)