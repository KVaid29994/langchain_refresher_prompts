from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

parser = JsonOutputParser()
# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


template = PromptTemplate(template = "Give me name , age and city of a fictional person\n{format_instruction}", input_variables=[], partial_variables={'format_instruction' : parser.get_format_instructions()})

prompt = template.format()

# print(prompt)

# result = model.invoke(prompt)
# print (result)

chain = template | model | parser
result = chain.invoke({})

# final_result = parser.parse(result.content)
print (result)






