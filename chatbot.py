from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_history =[SystemMessage(content = "You are a helpful assistant")]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input) )
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content =result.content))
    print ("AI: ",result.content)
print (chat_history)