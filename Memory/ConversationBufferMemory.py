import os
from dotenv import load_dotenv
from langchain.chains.conversation.base import ConversationChain
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

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

memory = ConversationBufferMemory()

memory.chat_memory.add_message(HumanMessage("Hi there!"))
memory.chat_memory.add_message(AIMessage("Hi there! It's nice to meet you. How can I help you today?"))

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)
conversation.invoke(input="I'm doing well! Just having a conversation with an AI.")
response=conversation.invoke(input="Tell me about yourself.")
print(response['response'])