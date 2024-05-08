# Sistema de Consulta Avanzada sobre la Mempool de Bitcoin

Este repositorio contiene dos programas principales que trabajan con la base de datos Chroma para manejar documentos relacionados con la mempool de Bitcoin. El primer programa se enfoca en la persistencia de documentos procesados y su indexación en una base de datos Chroma, y el segundo permite realizar consultas sobre estos documentos almacenados.

## Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Persistencia de Documentos en Chroma](#persistencia-de-documentos-en-chroma)
- [Consulta de Documentos](#consulta-de-documentos)
- [Instalación](#instalación)
- [Uso](#uso)

## Descripción del Proyecto

Este proyecto facilita la manipulación y consulta de documentos relacionados con la mempool de Bitcoin utilizando técnicas avanzadas de procesamiento de lenguaje natural y almacenamiento vectorial persistente. Se utilizan dos scripts principales para 1) almacenar documentos de forma persistente en una base de datos Chroma, y 2) consultar dichos documentos mediante un servidor de Streamlit.

## Persistencia de Documentos en Chroma

El primer script se encarga de la carga, procesamiento y almacenamiento persistente de documentos en una base de datos Chroma. Los documentos se dividen en fragmentos más manejables, se incrustan utilizando OpenAIEmbeddings y se almacenan en disco.

### Características Principales:
- **Carga y procesamiento de documentos:** Se carga un documento de texto sobre la mempool y se divide en fragmentos.
- **Incrustación y almacenamiento:** Se generan incrustaciones de los fragmentos y se almacenan en una base de datos Chroma persistente.

## Consulta de Documentos

El segundo script utiliza Streamlit para ofrecer una interfaz de usuario donde se pueden realizar consultas en lenguaje natural. Las consultas se procesan para recuperar la información relevante de los documentos almacenados en la base de datos Chroma.

### Funcionalidades:
- **Interfaz Streamlit:** Interfaz para ingresar consultas y mostrar respuestas.
- **Consulta de documentos incrustados:** Recupera documentos relevantes basados en la similitud de la consulta.

## Instalación

Para instalar y ejecutar los scripts, se requieren los siguientes pasos:

```bash
pip install -qU langchain
pip install -qU langchain-openai
pip install streamlit
```

## Uso

Para ejecutar el script de almacenamiento de documentos, simplemente ejecuta el primer script Python. Para iniciar la interfaz de consulta, ejecuta el segundo script utilizando Streamlit:

```bash
streamlit run script_consulta.py
```

## Contribuciones
Las contribuciones a estos apuntes serán bienvenidas, ya sea para mejorar las soluciones existentes, ofrecer nuevas perspectivas, o proponer nuevos desafíos. Por favor, siga las mejores prácticas de desarrollo y documentación al contribuir.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo `LICENSE.md` para más detalles.



