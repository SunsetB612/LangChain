import os
from dotenv import load_dotenv
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import SerpAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.agents import Tool


load_dotenv()
llm_api_key = os.getenv("MY_CHATECNU_API_KEY")
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

# 创建搜索工具，SerpAPI用于搜索信息
search = SerpAPIWrapper()

# 定义使用的工具
tools = [
    Tool(
        name = "Current Search",
        func=search.run,
        description="useful for when you need to answer questions about current events or the current state of the world"
    ),
]

#初始化一个会话内存
memory = ConversationBufferMemory(memory_key="chat_history")

llm = ChatOpenAI(
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
    api_key=llm_api_key,
    model="ecnu-plus",
    temperature=0
)
agent_chain = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,  # 定义代理类型
    verbose=True,  # 启用详细日志输出
    memory=memory,   # 使用会话内存
    handle_parsing_errors=True
)

agent_chain.run(input="hi, my name is Bob.")
print(memory.buffer)
agent_chain.run(input="what's my name?")
print(memory.buffer)  # 查看当前存储的会话历史
