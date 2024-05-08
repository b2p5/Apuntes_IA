# AI Blockchain SQL Chatbot

Este repositorio contiene un chatbot impulsado por IA, diseñado para facilitar consultas SQL en lenguaje natural sobre una base de datos que almacena estadísticas de Bitcoin. Utiliza la biblioteca LangChain para procesar las consultas y Streamlit para la interfaz de usuario.

## Descripción

Este chatbot permite a los usuarios realizar consultas complejas sobre una base de datos de estadísticas de Bitcoin sin necesidad de conocer SQL. El chatbot transforma preguntas en lenguaje natural a consultas SQL utilizando modelos de lenguaje de OpenAI, proporcionando una interfaz accesible y eficiente para el análisis de datos de blockchain.

## Características

- **Interfaz de usuario amigable:** Utiliza Streamlit para proporcionar una interfaz web donde los usuarios pueden ingresar sus consultas.
- **Procesamiento avanzado de lenguaje natural:** Convierte consultas de lenguaje natural en SQL utilizando LangChain y modelos de OpenAI.
- **Acceso directo a la base de datos SQL:** Realiza consultas sobre una base de datos SQLite que almacena estadísticas detalladas sobre transacciones de Bitcoin.

## Estructura de la Base de Datos

La base de datos `estadisticas_btc.db` contiene varios campos importantes:
- **med_20_num_txs:** Media móvil del número de transacciones de los últimos 20 bloques.
- **total_fee:** Comisión total de las transacciones en el bloque.
- **timestamp:** Fecha y hora de la transacción en formato timestamp.
- **date_time_str:** Fecha y hora de la transacción en formato año-mes-día hora:minutos:segundos.

## Instalación

Para instalar y ejecutar este chatbot en tu entorno local, sigue estos pasos:

1. Clona este repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias:
    ```bash
    pip install streamlit langchain langchain-openai
    ```
4. Crea un archivo `.env` en el directorio principal del proyecto con tu clave API de OpenAI:
    ```plaintext
    OPENAI_API_KEY='tu_clave_api_aquí'
    ```
5. Ejecuta la aplicación de Streamlit:
    ```bash
    streamlit run langChain_sql.py
    ```

## Uso

Una vez que la aplicación esté corriendo, simplemente ingresa tu consulta en el campo de texto y presiona el botón "Submit" para obtener resultados. El chatbot procesará la consulta y devolverá los resultados de la base de datos directamente en la interfaz de Streamlit.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si deseas mejorar el chatbot o agregar nuevas funcionalidades, considera realizar un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
