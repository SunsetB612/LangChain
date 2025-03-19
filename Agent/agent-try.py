import os

from dotenv import load_dotenv
from langchain.agents import initialize_agent,AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import ChatOpenAI


load_dotenv()
api_key = os.getenv("MY_CHATECNU_API_KEY")
serpapi_api_key=os.getenv("SERPAPI_API_KEY")

llm = ChatOpenAI(
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
    api_key=api_key,
    model="ecnu-plus",
    temperature=0
)

#加载工具集
tools = load_tools(
    tool_names=["serpapi"],#serpapi是Google搜索引擎API，llm-math是数学计算工具
    serpapi_api_key=serpapi_api_key
)
#创建智能体
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,#零样本提示策略
    verbose=True,  #开启日志
    handle_parsing_errors=True  # 自动处理解析错误
)
#response = agent.invoke("搜索上海2025年3月19日的天气是什么，然后计算 25 * 12 的结果")
response = agent.invoke("姚明的妻子是谁")
print(response)