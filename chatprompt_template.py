from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import SystemMessage, HumanMessage

chat_template =  ChatPromptTemplate([ 
    ('system', "you are a helpful {domain} expert"),('human',"explain in simple what is the {topic}")

])

prompt = chat_template.invoke({"domain": "cricekt expert", "topic":"dusra"})

print (prompt)