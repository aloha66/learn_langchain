# 导入必要的库
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# from langchain_community.llms import HuggingFaceEndpoint
# HuggingFaceEndpoint新的api，但报错，且为any
# Bad request:
# Error in `parameters.max_new_tokens`: ensure this value is less than or equal to 250
from langchain_community.llms import HuggingFaceHub


# 初始化HF LLM
llm = HuggingFaceHub(
    repo_id="google/flan-t5-small",
    # 报错
    # repo_id="meta-llama/Llama-2-7b-chat-hf",
)

# 创建简单的question-answering提示模板
template = """Question: {question}
              Answer: """

# 创建Prompt
prompt = PromptTemplate(template=template, input_variables=["question"])

# 调用LLM Chain --- 我们以后会详细讲LLM Chain
llm_chain = LLMChain(prompt=prompt, llm=llm)

# 准备问题
question = "Rose is which type of flower?"

# 调用模型并返回结果
print(llm_chain.invoke(question))
