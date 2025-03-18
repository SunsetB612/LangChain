import os
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import messages_from_dict, messages_to_dict
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI

import warnings
warnings.filterwarnings("ignore")


load_dotenv()
api_key = os.getenv("MY_CHATECNU_API_KEY")

llm = ChatOpenAI(
    base_url="https://chat.ecnu.edu.cn/open/api/v1",
    api_key=api_key,
    model="ecnu-plus",
    temperature=0
)

history=ChatMessageHistory()

history.add_message(HumanMessage("请用小猫的口吻回答所有问题"))
history.add_message(AIMessage("好的，我将用小猫的口吻回答你的所有问题"))

dicts = messages_to_dict(history.messages)
print(dicts)
new_messages = messages_from_dict(dicts)
print(new_messages)

response = llm.invoke(new_messages+[HumanMessage("今天天气怎么样")])
print(response.content)