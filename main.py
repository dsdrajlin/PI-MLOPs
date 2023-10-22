import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/PTG/{genero}")
def PlayTimeGenre( genero : str ):
    df = pd.read_csv("./Datasets_API/PlayTimeGenre.csv")
    anio = int(df.loc[df[genero].idxmax()]["year"])
    return {f"Año de lanzamiento con más horas jugadas para Género {genero}" : anio}