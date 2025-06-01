from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


load_dotenv()


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

messages = [SystemMessage(content = "You are an helpful assistant"),
            HumanMessage(content = "Tell me about Langchain")]

result = model.invoke(messages)
messages.append(AIMessage(content = result.content))
print (messages)