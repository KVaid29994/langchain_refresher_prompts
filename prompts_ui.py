from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

st.header("Research Assistant")
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt("template.json")

# prompt = template.invoke({'paper_input': paper_input, "style_input": style_input,"length_input": length_input})


llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)


if st.button("Summarize"):
    chain = template | model
    result = chain.invoke({'paper_input': paper_input, "style_input": style_input,"length_input": length_input})
    # prompt = template.invoke({'paper_input': paper_input, "style_input": style_input,"length_input": length_input})
    # result = model.invoke(prompt)
    st.write (result.content)
