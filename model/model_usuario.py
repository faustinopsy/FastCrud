from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UsuarioCreate(BaseModel):
    id: Optional[UUID] = None 
    nome: str
    senha: str
    email: str

class UsuarioUpdate(BaseModel):
    nome: str
    senha: str

