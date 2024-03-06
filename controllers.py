from typing import List, Optional
from pydantic import BaseModel, ValidationError
import uuid
import json


class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool = False


def _load_items() -> List[Item]:
    try:
        with open("items_db.txt", "r") as file:
            return [Item.parse_raw(line) for line in file]
    except FileNotFoundError:
        return []


def _save_items(items: List[Item]):
    with open("items_db.txt", "w") as file:
        for item in items:
            file.write(f"{item.json()}\n")


def create_item(item: Item) -> Item:
    item.id = str(uuid.uuid4())  
    items = _load_items()
    items.append(item)
    _save_items(items)
    return item

def get_all_items() -> List[Item]:
    return _load_items()

def update_item(item_id: str, updated_item: Item) -> Optional[Item]:
    items = _load_items()
    for i, item in enumerate(items):
        if item.id == item_id:
            updated_item.id = item_id  
            items[i] = updated_item
            _save_items(items)
            return updated_item
    return None

def delete_item(item_id: str) -> dict:
    items = _load_items()
    items = [item for item in items if item.id != item_id]
    if len(items) < len(_load_items()):
        _save_items(items)
        return {"message": "Item excluido com sucesso"}
    else:
        return {"message": "Item não encontrado, não poderá excluir"}