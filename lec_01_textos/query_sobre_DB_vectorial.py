# -*- coding: utf-8 -*-

# Importar Streamlit
import streamlit as st

# Importar librerías
from pydantic import BaseModel, Field
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.agents import AgentExecutor
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.tools import StructuredTool
from langchain_openai import ChatOpenAI

from langchain_community.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import VectorDBQA


# Cargar la clave de la API de OpenAI desde el archivo .env
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
openai_api_key = os.environ.get('OPENAI_API_KEY')



# Funciones
def get_query_document(query: str) -> str:
    """
    Retrieve response find into persist_directory.

    Args:
        query (str): The query to find .

    Returns:
        str: The full name of the customer.
    """

    persist_directory = './Chroma/db_mempool'
    embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma(persist_directory=persist_directory, 
                      embedding_function=embedding
                      )


    docs = vectordb.similarity_search(query, k=2)
    
    return docs[0].page_content
    



class GetQueryDocument(BaseModel):
    """
    Pydantic arguments schema for get_query_document method
    """
    query: str = Field(..., description="The query to find in DocumentacionMempool.txt vectorized")



system_init_prompt = """
    Dada la pregunta sobre la mempool, respóndela lo mejor que puedas, basándose en la función 
    get_query_document.
    Encuentre la respuesta a la pregunta en el documento vectorizado en db_mempool.
    Responde en español.
    """

user_init_prompt = """
    La pregunta es: {}.
    Go!
    """

from langchain_core.utils.function_calling import convert_to_openai_function

# Initialize the LLM
llm = ChatOpenAI(
    temperature=0.1,
    model_name="gpt-3.5-turbo-1106",
    openai_api_key=openai_api_key,
)

# Initialize the tools
tools = [
    
    StructuredTool.from_function(
        func=get_query_document,
        args_schema=GetQueryDocument,
        description="Function to response questions about mempool.",
    )
]

llm_with_tools = llm.bind(
    functions=[convert_to_openai_function(t) for t in tools]
)

# Initialize the prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_init_prompt),
        ("user", user_init_prompt.format("{input}")),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ],
)

# Inicializa el agente con una pipeline.
agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
    }
    | prompt  
    | llm_with_tools  
    | OpenAIFunctionsAgentOutputParser()  
)


# Initialize the agent executor
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               verbose=True)


# Streamlit app
def main():
    st.title('AI Mempool')
    query = st.text_input('Enter your query:', '')

    if st.button('Submit'):
        with st.spinner('Fetching response...'):
            response = agent_executor.invoke({"input": query})
            result = response.get("output", "No response available.")
            st.write('Response:', result)

if __name__ == "__main__":
    main()

