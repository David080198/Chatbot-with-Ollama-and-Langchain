# Importa la clase ChatOpenAI del módulo langchain_openai
# Esta clase se utiliza para interactuar con el modelo de lenguaje OpenAI.
from langchain_openai import ChatOpenAI

# Importa la clase ChatPromptTemplate del módulo langchain_core.prompts
# Esta clase se utiliza para crear plantillas de solicitud de chat, las cuales pueden 
# estructurar y formatear las preguntas o mensajes que se envían al modelo de lenguaje.
from langchain_core.prompts import ChatPromptTemplate

# Importa la clase StrOutputParser del módulo langchain_core.output_parsers
# Esta clase se utiliza para analizar y procesar las respuestas de salida del modelo de lenguaje, 
# convirtiéndolas en un formato de cadena de texto.
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

with open('.env', 'r') as file:
    print(file.read())

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("Search the topic u want")

# openAI LLm 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))