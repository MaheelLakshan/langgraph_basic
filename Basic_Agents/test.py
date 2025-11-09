import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = llm.invoke([HumanMessage(content=user_input)])
    print("AI:", response.content)
