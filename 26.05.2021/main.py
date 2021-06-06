from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.counter = 0


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    code: str
    tax: Optional[str] = None


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/")
def hello():
    return {"message": "Witaj Świecie!"}


@app.get("/hello/{name}")
def hello_name(name):
    return {"message": f'Hello {name}'}


@app.get("/counter")
def counter():
    app.counter += 1
    return {"counter": str(app.counter)}


def add_item():
    pass
