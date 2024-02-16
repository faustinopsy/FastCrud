from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Item(BaseModel):
    id: Optional[UUID] = None
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool = False
