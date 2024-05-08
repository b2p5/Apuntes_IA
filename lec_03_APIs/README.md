# Ask Mempool Space with AI

Este repositorio contiene una aplicación desarrollada con Streamlit y LangChain, diseñada para permitir a los usuarios hacer consultas en lenguaje natural sobre datos de la blockchain de Bitcoin utilizando la API de Mempool Space.

## Descripción del Proyecto

Esta aplicación transforma preguntas formuladas en lenguaje natural en consultas API que recuperan información sobre bloques de la blockchain de Bitcoin. Utiliza modelos de lenguaje avanzados de OpenAI para procesar las preguntas y estructurar las respuestas de manera efectiva.

## Características Principales

- **Interfaz de Usuario Streamlit**: Proporciona una interfaz web sencilla para ingresar consultas y recibir respuestas.
- **Integración con la API de Mempool Space**: Accede a datos en tiempo real sobre la blockchain de Bitcoin, incluyendo el último bloque, detalles de bloques específicos, y estadísticas de tarifas.
- **Procesamiento Avanzado de Lenguaje Natural**: Usa LangChain y OpenAI para interpretar preguntas en lenguaje natural y formular respuestas claras y precisas.

## Funciones de la API

El programa proporciona las siguientes funcionalidades específicas:

- **Obtener el número del último bloque**: Devuelve el número del último bloque en formato JSON.
- **Obtener el hash de un bloque específico**: Dado el número de un bloque, devuelve su hash.
- **Obtener detalles de un bloque específico**: Dado el hash de un bloque, devuelve detalles como el tamaño del bloque, el tiempo de confirmación, y más.
- **Obtener tarifas promedio por bloque**: Devuelve las tarifas promedio y la altura promedio de los bloques durante un período específico.

## Instalación

Para instalar y ejecutar esta aplicación en tu entorno local, sigue estos pasos:

1. Clona este repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install streamlit langchain langchain-openai requests pydantic
   ```


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

Una vez que la aplicación está ejecutando, ingresa tu consulta en el campo de texto y presiona "Submit". El sistema procesará tu consulta y mostrará los resultados directamente en la interfaz de Streamlit.

## Contribuciones

Las contribuciones a este proyecto son bienvenidas. Si deseas mejorar el chatbot o agregar nuevas funcionalidades, considera realizar un fork del repositorio y enviar un pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.




