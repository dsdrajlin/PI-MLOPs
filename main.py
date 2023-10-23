import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/PTG/{genero}")
def PlayTimeGenre( genero : str ):
    # Crear un dataframe donde las filas son géneros y las columnas años.
    df = pd.read_csv("./Datasets_API/PlayTimeGenre.csv")

    # Encontrar la columna con el mayor valor para la fila género.
    anio = int(df.loc[df[genero].idxmax()]["year"])
    return {f"Año de lanzamiento con más horas jugadas para Género {genero}" : anio}

@app.get("/SA/{anio}")
def sentiment_analysis( anio : int ):
    # Crear un dataframe donde las filas son años y las columnas análisis de sentimiento.
    df = pd.read_csv("./Datasets_API/sentiment_analysis.csv")

    # Encontrar los valores de sentimiento para el año pasado como parámetro.
    negativo = df.loc[df.year == anio, "0"].item()
    neutral = df.loc[df.year == anio, "1"].item()
    positivo = df.loc[df.year == anio, "2"].item()

    return {"Negative" : negativo, "Neutral" : neutral, "Positive" : positivo}