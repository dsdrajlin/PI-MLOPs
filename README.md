<img src="./assets/steam_logo.jpeg">

<h1 align="center"><b> Steam Game Recommender </b></h1>
<hr>

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

| Librería | Uso |
|:---:|---|
| <img src="./assets/pandas_logo.png" width="100"> <img src="./assets/numpy_logo.png" width="100"> | Operaciones con Series y DataFrames |
| <img src="./assets/matplotlib_logo.svg" width="100"> <img src="./assets/seaborn_logo.svg" width="100"> | Graficación |
| <img src="./assets/sklearn_logo.png" width="100"> | Procesamiento de datos y aprendizaje automático |
| <img src="./assets/textblob_logo.png" width="100"> | Análisis de sentimientos |
| <img src="./assets/PyPI_logo.png" width="100"><br>(wordcloud/langdetect)| Operaciones sobre texto |
| <img src="./assets/fastapi_logo.png" width="100"> <img src="./assets/uvicorn_logo.png" width="100"> | Montado de la API |

Adicionalmente se hizo uso del sitio [__render.com__](https://render.com/) para el despliegue de la API.

## Archivos
Los principales archivos de este repositorio son:
* <a href="Diccionario de Datos STEAM.xlsx" download="Diccionario de Datos STEAM.xlsx">Diccionario de Datos STEAM.xlsx</a>: Información sobre la estructura de los 3 archivos de origen (no incluidos en el repositorio).
* [ETL.ipynb](ETL.ipynb): ETL de los 3 archivos de origen, junto con un EDA de los mismos.
* [API.ipynb](API.ipynb): Archivo donde se generan los archivos de consulta de la API.
* [RS.ipynb](RS.ipynb): Desarrollo del sistema de recomendación.
* [Datasets_API](Datasets_API/): Carpeta con los archivos de consulta de la API.
* [main.py](main.py): Funciones de la API.
* [assets](assets/): Imágenes del README.

## Demo
En este [video](https://youtu.be/zsVhxv65iCk) se muestra el esquema general de trabajo y las consultas a la API.

## Despliegue de la API
En este [link](https://pi-mlops-4j8c.onrender.com/docs) se podrá acceder a la API y realizar consultas. (Nota: al estar incorporado en una capa gratuita, puede demorar unos minutos en levantar el servicio)