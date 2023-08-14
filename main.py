from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi app con platzi"
app.version = "0.0.1"


class Movie(BaseModel):
    name: str
    id: Optional[int] = None
    category: str


movies = [
    {"name": "pelicula_a", "id": 3, "category": "thriller"},
    {"name": "pelicula", "id": 5, "category": "action"},
    {"name": "pelicula_s", "id": 1, "category": "comedy"},
    {"name": "pelicula_b", "id": 2, "category": "comedy"},
]


@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>HOLA AMIGO</h1>")


@app.get("/Movies", tags=["Movies"])
def get_movies():
    return movies


@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return id


@app.get("/movies/", tags=["Movies"])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item["category"] == category]


@app.post("/movies", tags=["Movies"])
def create_movies(movie: Movie):
    movies.append(movie)
    return movies


@app.put("/movies/{id}", tags=["Movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["name"] = movie.name
            item["category"] = movie.category
            return movies


@app.delete("/movies/{id}", tags=["Movies"])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
