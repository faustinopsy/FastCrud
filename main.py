from fastapi import FastAPI
from model.model_item import Item
from controller.controller_item import create_item, get_all_items, update_item, delete_item
from config.helper import add_cors

app = FastAPI()

add_cors(app)

@app.post("/items/")
def add_item(item: Item):
    return create_item(item)

@app.get("/items/")
def read_items():
    return get_all_items()

@app.put("/items/{item_id}")
def update_item_details(item_id: str, item: Item):
    return update_item(item_id, item)

@app.delete("/items/{item_id}")
def remove_item(item_id: str):
    return delete_item(item_id)
