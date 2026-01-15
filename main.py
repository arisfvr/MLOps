from typing import Union

from fastapi import FastAPI

app = FastAPI()

def score(): 
    return 1


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def surface(item_id: int):
    q = score()
    return {q}