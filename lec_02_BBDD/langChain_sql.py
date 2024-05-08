# Get openai_api_key
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)
openai_api_key = os.environ.get('OPENAI_API_KEY')


# Importar Streamlit
import streamlit as st

from langchain_community.utilities.sql_database import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///./bbdd/estadisticas_btc.db")

# Agente
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI

toolkit = SQLDatabaseToolkit(db=db, 
                             llm=ChatOpenAI(temperature=0), 
                             openai_api_key=openai_api_key)
context = toolkit.get_context()
tools = toolkit.get_tools()



from langchain_community.agent_toolkits.sql.prompt import SQL_FUNCTIONS_SUFFIX
from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts.chat import (
                                            ChatPromptTemplate,
                                            HumanMessagePromptTemplate,
                                            MessagesPlaceholder,
                                        )

messages = [
    SystemMessage(content=
        "Eres un experto en SQL y bases de datos. " +
        "Muestra todos los resultados, por muy extensa que sea la tabla. " +
        "Ayudame a hacer consultas SQL sobre la base de datos de estadísticas de Bitcoin (estadisticas_btc). " +
        "El campo \"med_20_num_txs\" contiene la media movil del numero de transacciones de los últimos 20 Bloques.capitalize" +
        "El campo \"total_fee\" contiene la comisión total de las transacciones en el bloque."+
        "El campo \"timestamp\" contiene la fecha y hora de la transacción en formato timestamp."+
        "El campo \"date_time_str\" contiene el año-mes-dia hora:minutos:segundos de la transacción."+
        "Contesta en español y de forma clara y concisa."),
    HumanMessagePromptTemplate.from_template("{input}"),
    AIMessage(content=SQL_FUNCTIONS_SUFFIX),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
]

prompt = ChatPromptTemplate.from_messages(messages)
prompt = prompt.partial(**context)



from langchain.agents import create_openai_tools_agent
from langchain.agents.agent import AgentExecutor

llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0)

agent = create_openai_tools_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
)


# Streamlit app
def main():
    st.title('AI Blockchain SQL Chatbot')
    query = st.text_area('Enter your query:', height=75  ,
            value='Dame en formato de tabla con dos columnas, la hora  y total_fee por hora, para el día 20 de abril de 2024.'
            #value='Dame en formato de tabla con tres columnas, la fecha, la media movil de los 20 ultimos bloques para el numero de txs y total_fee, para el día 20 de abril de 2024.'
    
    )
                          
    if st.button('Submit'):
        with st.spinner('Fetching response...'):
            response = agent_executor.invoke({"input": query})
            result = response.get("output", "No response available.")
            st.write('Response:', result)

if __name__ == "__main__":
    main()