from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

banco_dados = [
    {"id": 1, "name": "Notebbok", "price": 4500.00},
    {"id": 2, "name": "Mouse sem Fio", "price": 150.00},
]

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool | None = True

@app.get("/")
def home():
    return {"message": "Bem-vindo à minha primeira API em Python!"}

@app.get("/items")
def list_Itmes():
    return banco_dados

@app.get("/items/{item_id}")
def search_Item(item_id: int):
    for item in banco_dados:
        if item["id"] == item_id:
            return item
    return {"erro": "Item not found"}

@app.post("/itmes")
def creat_item(item: Item):
    new_item = item.dict()
    new_item["id"] = len(banco_dados) + 1
    banco_dados.append(new_item)
    return {"message": "Item successfully added!", "item": new_item}