![](https://upload.wikimedia.org/wikipedia/commons/8/87/New_Steam_Logo_with_name.jpg)

<h1 align="center"><b> Steam Game Recommender </b></h1>


## Tabla de contenidos  <!-- omit in toc -->
- [Descripción](#descripción)
- [Objetivos](#objetivos)
- [Stack tecnológico](#stack-tecnológico)
- [Archivos](#archivos)


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
* [ETL.ipynb](ETL.ipynb)
* 