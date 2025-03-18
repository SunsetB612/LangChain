import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage,AIMessage

load_dotenv()
api_key = os.getenv("MY_CHATECNU_API_KEY")

llm = ChatOpenAI(
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
    api_key=api_key,
    model="ecnu-plus"
)

history = ChatMessageHistory()

history.add_message(HumanMessage("请用小猫的口吻回答所有问题"))
history.add_message(AIMessage("好的，我将用小猫的口吻回答你的所有问题"))

messages = history.messages+[HumanMessage("今天天气怎么样")]

response = llm.invoke(messages)
print(response.content)