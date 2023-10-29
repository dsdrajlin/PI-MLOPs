![](https://upload.wikimedia.org/wikipedia/commons/8/87/New_Steam_Logo_with_name.jpg)

<h1 align="center"><b> Steam Game Recommender </b></h1>


## Tabla de contenidos  <!-- omit in toc -->
- [Descripción](#descripción)
- [Objetivos](#objetivos)
- [Stack tecnológico](#stack-tecnológico)
- [Archivos](#archivos)
- [Demo](#demo)
- [Despliegue de la API](#despliegue-de-la-api)


## Descripción
En este proyecto se realizó un sistema de recomendación de juegos de la plataforma STEAM. Para ello se contó con bases de datos obtenidas de la misma plataforma, se realizó un ETL, se hizo un análisis descriptivo de los mismos y se usaron como fuente para la construcción de un modelo de aprendizaje automático. Este trabajo fue disponibilizado a través de una REST API y deployado a través de un servicio web.

## Objetivos
* Extraer, transformar y cargar los datos (`ETL`).
* Hacer un análisis exploratorio de los datos (`EDA`).
* Realizar `análisis de sentimientos` de las reviews de los usuarios.
* Montar y desplegar una `API` capaz de responder GET requests.
* Crear un `modelo de aprendizaje automático` como sistema de recomendación.

## Stack tecnológico
El proyecto está llevado a cabo en `python` en archivos .py y .ipynb. Algunas de 
las librerias destacadas son:
* __json/gzip/ast__: lectura de archivos.
* __pandas/numpy__: operaciones sobre DataFrames.
* __matplotlib/seaborn__: graficación.
* __scikit-learn__: procesamiento de datos y aprendizaje automático.
* __textblob__: análisis de sentimientos.
* __langdetect/wordcloud__: operaciones sobre texto.
* __fastapi/uvicorn__: montado de la API.

Adicionalmente se hizo uso del sitio __render.com__ para el despliegue de la API.

## Archivos
Los principales archivos de este repositorio son:
* <a href="Diccionario de Datos STEAM.xlsx" download="Diccionario de Datos STEAM.xlsx">Diccionario de Datos STEAM.xlsx</a>: Información sobre la estructura de los 3 archivos de origen (no incluidos en el repositorio).
* [ETL.ipynb](ETL.ipynb): ETL de los 3 archivos de origen, junto con un EDA de los mismos.
* [API.ipynb](API.ipynb): Archivo donde se generan los archivos de consulta de la API.
* [Datasets_API](Datasets_API/): Carpeta con los archivos de consulta de la API
* [main.py](main.py): Funciones de la API.
* [RS.ipynb](RS.ipynb): Desarrollo del sistema de recomendación.

## Demo
En este [video](https://drive.google.com/file/d/1hYPQDf2RY5MB4PU3TGX8L9DlJ8vP-32b/view?usp=sharing) se muestra el esquema general de trabajo y las consultas a la API.

## Despliegue de la API
En este [link](https://pi-mlops-4j8c.onrender.com/docs) se podrá acceder a la API y realizar consultas.