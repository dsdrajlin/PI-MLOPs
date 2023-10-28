import pandas as pd
import numpy as np
from fastapi import FastAPI

description = "Esta API permite realizar consultas referidas a la plataforma STEAM."

app = FastAPI(title="STEAM API",
              description=description,
              contact={"name": "Sebastian Drajlin",
                       "url": "https://github.com/dsdrajlin/PI-MLOps",
                       "email": "dsdrajlin@gmail.com"})


@app.get("/PTG/{genero}")
def PlayTimeGenre(genero: str):
    """
    Retornar el género mas jugado por año.
    """
    # Crear un dataframe donde las filas son años y las columnas géneros.
    df = pd.read_csv("./Datasets_API/PlayTimeGenre.csv")

    # Encontrar la fila con el mayor valor para la columna género.
    anio = int(df.loc[df[genero].idxmax()]["year"])
    return {f"Año de lanzamiento con más horas jugadas para Género {genero}" : anio}


@app.get("/UFG/{genero}")
def UserForGenre (genero: str):
    """
    Retornar el usuario que más jugó a un género y cuántas horas jugó cada año.
    """
    # Crear un dataframe donde las filas son user_id y las columnas géneros.
    df1 = pd.read_csv("./Datasets_API/UserForGenre1.csv")

    # Encontrar la fila con el mayor valor para la columna género.
    user = df1.loc[df1[genero].idxmax()]["user_id"]

    # Crear un dataframe donde las filas son años y las columnas usuarios.
    df2 = pd.read_csv("./Datasets_API/UserForGenre2.csv")

    res = [] # Crear una lista vacia para almacenar los pares año-horas jugadas.

    # Iterar a traves de las filas del dataframe.
    for index, row in df2.iterrows():
        anio = row['review_year']  # Obtener la fila del año.
        horas = round(row[user], 2)  # Obtener horas jugadas para año y user.

        if horas >= 0:
            res.append({anio: horas})

    return {f"Usuario con más horas jugadas para Género {genero}" : user,
            "Horas jugadas": res}


@app.get("/UR/{anio}")
def UsersRecommend(anio: int):
    """
    Retornar los 3 juegos mas recomendados para el año dado.
    """
    # Crear un dataframe con columnas "review_year" (año), "app_name" y 
    # "recommend" (número de recomendaciones). Solo incluye los 3 juegos 
    # mas recomendados por año.
    df = pd.read_csv("./Datasets_API/UsersRecommend.csv")

    if anio in df.review_year.unique(): # Verificar que el año esté presente.
        # Crear un dataframe filtrando por anio (solo 3 filas).
        mejores = df[df.review_year == anio].reset_index()

        primero = mejores.loc[0, "app_name"] # Primer juego mas recomendado.
        segundo = mejores.loc[1, "app_name"] # Segundo juego mas recomendado.
        tercero = mejores.loc[2, "app_name"] # Tercer juego mas recomendado.

        return [{"Puesto 1" : primero}, {"Puesto 2" : segundo},{"Puesto 3" : tercero}]
    else:
        return "Año no encontrado. Intente otro año."


@app.get("/UNR/{anio}")
def UsersNotRecommend(anio: int):
    """
    Retornar los 3 juegos menos recomendados para el año dado.
    """
    # Crear un dataframe con columnas "review_year" (año), "app_name" y 
    # "score_not_recommend" (score de recomendaciones negativas).
    df = pd.read_csv("./Datasets_API/UsersNotRecommend.csv")

    if anio in df.review_year.unique(): # Verificar que el año esté presente.
        # Filtrado df por año y ordenar por "score_not_recommend" ascendente.
        peores = df[df.review_year == anio].sort_values("score_not_recommend",
                                                         ascending=False)
        peores.reset_index(drop=True, inplace=True) # Resetear el indice.

        primero = peores.loc[0, "app_name"] # Primer juego menos recomendado.
        segundo = peores.loc[1, "app_name"] # Segundo juego menos recomendado.
        tercero = peores.loc[2, "app_name"] # Tercer juego menos recomendado.

        return [{"Puesto 1" : primero}, {"Puesto 2" : segundo},{"Puesto 3" : tercero}]
    else:
        return "Año no encontrado. Intente otro año."


@app.get("/SA/{anio}")
def sentiment_analysis(anio: int):
    """
    Retornar el número de reviews negativas, neutrales y positivas para un año dado.
    """
    # Crear un dataframe donde las filas son años y las columnas análisis de sentimiento.
    df = pd.read_csv("./Datasets_API/sentiment_analysis.csv")

    # Encontrar los valores de sentimiento para el año pasado como parámetro.
    negativo = df.loc[df.year == anio, "0"].item()
    neutral = df.loc[df.year == anio, "1"].item()
    positivo = df.loc[df.year == anio, "2"].item()

    return {"Negative" : negativo, "Neutral" : neutral, "Positive" : positivo}

@app.get("/RG/{id_ref}")
def recomendacion_juego(id_ref: int):
    """
    Recibe un id de juego y retorna 5 juegos similares recomendados.
    """
    # Crear un dataframe a partir "top_5_recomendados.json".
    # Las columnas son los id del juego de referencia y las 5 filas los id
    # de los juegos mas similares.
    df = pd.read_json("./Datasets_API/top_5_recomendados.json")

    # Crear un dataframe a partir "id_name.csv".
    id_name_df = pd.read_csv("./Datasets_API/id_name.csv")

    res = {} # Crear un diccionario vacio para ser retornado como json.

    # df[id_ref] es una serie de Pandas correspondiente a la columna "id_ref"
    # del dataframe df. "val" contiene los id de los juegos
    for idx, val in df[id_ref].items():
        # Se obtiene el nombre del juego.
        name = id_name_df[id_name_df.id == val].app_name.item()
        # Se guarda en el diccionario el id como llave y el nombre como valor.
        res[val] = name

    return res