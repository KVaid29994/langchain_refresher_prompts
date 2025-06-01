from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

# Step 1: Create the chat template
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Step 2: Parse the chat history from file
chat_history = []

with open("chat_history.txt", "r", encoding="utf-8") as f:
    buffer = ""
    sender = None

    for line in f:
        line = line.strip()
        if line.startswith("**Human:**"):
            if buffer and sender == "AI":
                chat_history.append(AIMessage(content=buffer.strip()))
            elif buffer and sender == "Human":
                chat_history.append(HumanMessage(content=buffer.strip()))
            buffer = line[len("**Human:**"):].strip()
            sender = "Human"
        elif line.startswith("**AI:**"):
            if buffer and sender == "Human":
                chat_history.append(HumanMessage(content=buffer.strip()))
            elif buffer and sender == "AI":
                chat_history.append(AIMessage(content=buffer.strip()))
            buffer = line[len("**AI:**"):].strip()
            sender = "AI"
        else:
            buffer += " " + line.strip()

    # append the last message
    if buffer:
        if sender == "Human":
            chat_history.append(HumanMessage(content=buffer.strip()))
        elif sender == "AI":
            chat_history.append(AIMessage(content=buffer.strip()))

# Step 3: Create the prompt
response = chat_template.invoke({
    "chat_history": chat_history,
    "query": "what did I make?"
})

print(response)
