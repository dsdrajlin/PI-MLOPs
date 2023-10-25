import pandas as pd

from fastapi import FastAPI

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


@app.get("/SA/{anio}")
def sentiment_analysis(anio: int):
    # Crear un dataframe donde las filas son años y las columnas análisis de sentimiento.
    df = pd.read_csv("./Datasets_API/sentiment_analysis.csv")

    # Encontrar los valores de sentimiento para el año pasado como parámetro.
    negativo = df.loc[df.year == anio, "0"].item()
    neutral = df.loc[df.year == anio, "1"].item()
    positivo = df.loc[df.year == anio, "2"].item()

    return {"Negative" : negativo, "Neutral" : neutral, "Positive" : positivo}