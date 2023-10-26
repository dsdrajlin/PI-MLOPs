import pandas as pd
import numpy as np
from fastapi import FastAPI
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()


@app.get("/PTG/{genero}")
def PlayTimeGenre(genero: str):
    # Crear un dataframe donde las filas son años y las columnas géneros.
    df = pd.read_csv("./Datasets_API/PlayTimeGenre.csv")

    # Encontrar la fila con el mayor valor para la columna género.
    anio = int(df.loc[df[genero].idxmax()]["year"])
    return {f"Año de lanzamiento con más horas jugadas para Género {genero}" : anio}


@app.get("/UFG/{genero}")
def UserForGenre (genero: str):
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
    # Crear un dataframe donde las filas son años y las columnas análisis de sentimiento.
    df = pd.read_csv("./Datasets_API/sentiment_analysis.csv")

    # Encontrar los valores de sentimiento para el año pasado como parámetro.
    negativo = df.loc[df.year == anio, "0"].item()
    neutral = df.loc[df.year == anio, "1"].item()
    positivo = df.loc[df.year == anio, "2"].item()

    return {"Negative" : negativo, "Neutral" : neutral, "Positive" : positivo}

@app.get("/RG/{id_ref}")
def recomendacion_juego(id_ref: int):
    # Cargar como dataframe el archivo "recomendacion_juego.csv".
    df = pd.read_csv("./Datasets_API/recomendacion_juego.csv")

    # Crear un dataframe cuya única fila sea aquella que que contiene el id del
    # juego pasado como parámetro y las columnas seleccionadas.
    fila_juego = df.loc[df.id == id_ref,
                         "genres_Accounting":"specs_Windows Mixed Reality"]
    
    # Calcular las similitudes del coseno entre este juego y los demas y 
    # guardarlos en un array de NumPy.
    scores_similitud = cosine_similarity(fila_juego,
                                          df.loc[:, "genres_Accounting":
                                                 "specs_Windows Mixed Reality"])
    
    # Convertir "scores_similitud" a un dataframe.
    similitud_df = pd.DataFrame(scores_similitud, columns=df.app_name,
                            index=df[df.id == id_ref].app_name)
    
    # Crear una serie en la que se ordenan los juegos de forma descendente 
    # según su similitud del coseno con el juego de referencia.
    recommended_games = similitud_df.iloc[0].sort_values(ascending=False)

    # Crear un diccionario vacio para ser retornado.
    res = {}

    # Iterar a través de los primeros 5 elementos (excluyendo el propio juego)
    # y obtener su nombre e id.
    for idx, val in recommended_games[1:6].items():
        app_name = idx
        item_id = df.loc[df.app_name == app_name, "id"].item()
        res[item_id] = app_name

    return res