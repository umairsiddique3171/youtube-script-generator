# Importing dependencies
import os 
import json
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
# from langchain.utilities import WikipediaAPIWrapper 

with open('api_key.json','r') as f:
    api_key = json.load(f)

os.environ['OPENAI_API_KEY'] = api_key.get('api_key')


# App Framework
st.title("🦜️🔗 Youtube Script Generator")
prompt = st.text_input("Please enter your video topic here")

# Llms 
llm = ChatOpenAI(temperature=0.9)

if prompt:
    response = llm.invoke(prompt)
    st.write(response)