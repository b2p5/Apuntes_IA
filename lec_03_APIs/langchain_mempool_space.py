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

# Para hacer Preguntas
import requests
# from langchain_openai import OpenAI




# Cargar la clave de la API de OpenAI desde el archivo .env
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
openai_api_key = os.environ.get('OPENAI_API_KEY')



# Funciones
def get_last_block() -> str:
  """
  Given the last blosk in format json.  
  Args:
      nulls  
  Returns:
      str: The JSON range weights.
  """
  respu = requests.get('https://mempool.space/api/blocks/tip/height')
  datos = respu.json()

  return datos


def get_hash_of_block(block:int) -> str:
  """
  Given the hash of blosk in format json.  
  Args:
      block: The block number.  
  Returns:
      str: The JSON range weights.
  """

  respu = requests.get('https://mempool.space/api/block-height/' + str(block))

  return respu.content


def get_details_about_block (block:str) -> str:
  """
  Given the details of a block in format json.  
  Args:
      block: The block hash.  
  Returns:
      str: The JSON range weights.
  """

  respu = requests.get('https://mempool.space/api/block/' + block)

  return respu.content


def get_average_total_fees_x_block() -> str:
  """
  Given the average total fees per block in format json.  
  Args:
      nulls  
  Returns:
      str: The JSON range weights.
  """

  respu = requests.get('https://mempool.space/api/v1/mining/blocks/fees/1w')
  datos = respu.json()

  return datos




class GetLastBlock(BaseModel):
    """
    Pydantic arguments schema for get_last_block method
    """

class GetHashOfBlock(BaseModel):
    """
    Pydantic arguments schema for get_hash_of_block method
    """
    block: int = Field(..., title="Block number", description="The block number")

class GetDetailsAboutBlock(BaseModel):
    """
    Pydantic arguments schema for get_details_about_block method
    """
    block: str = Field(..., title="Block hash", description="The block hash")

class GetAverageTotalFeesXBlock(BaseModel):
    """
    Pydantic arguments schema for get_average_total_fees_x_block method
    """




system_init_prompt = """
    Get the the block number of the last block, from the Bitcoin blockchain. Give it to me in JSON format.
    Get the hash of a block knowing the block number, from the Bitcoin blockchain. Give it to me in JSON format.
    Get the details of a block knowing the hash of the block, from the Bitcoin blockchain. Give them to me in JSON format.
    Get the average fees and average Height per block from the Bitcoin blockchain in JSON format.
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

# Initialize the tools for Agent
tools = [
    StructuredTool.from_function(
        func=get_last_block,
        args_schema=GetLastBlock,
        description="Function to get the block number of the last block",
    ),
    StructuredTool.from_function(
        func=get_hash_of_block,
        args_schema=GetHashOfBlock,
        description="Function to get the hash of a block knowing the block number",
    ),
    StructuredTool.from_function(
        func=get_details_about_block,
        args_schema=GetDetailsAboutBlock,
        description="Function to get the details of a block knowing the hash of the block",
    ),
    StructuredTool.from_function(
        func=get_average_total_fees_x_block,
        args_schema=GetAverageTotalFeesXBlock,
        description="Function to get the average total fees and average Height per block",
    ),
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
    st.title('Ask Mempool Space with AI')
    query = st.text_input('Enter your query:', 
                          'Give me the details of a last block.')
                        #   'Give me the hash of a last block.')
                        #   'Give me the height of a last block.')

    if st.button('Submit'):
        with st.spinner('Fetching response...'):
            response = agent_executor.invoke({"input": query})
            result = response.get("output", "No response available.")
            st.write('Response:', result)


if __name__ == "__main__":
    main()

