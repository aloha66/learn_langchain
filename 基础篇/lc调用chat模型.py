from langchain_openai import ChatOpenAI

llm = ChatOpenAI(  
    model="gpt-3.5-turbo",
    base_url="https://api.chatanywhere.tech/v1",
    temperature=0.8,
    max_tokens=60,)
response = llm.invoke("请给我的花店起个名")
print(response)