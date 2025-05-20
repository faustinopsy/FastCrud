from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class UsuarioCreate(BaseModel):
    id: Optional[UUID] = None 
    nome: str
    senha: str
    email: str
    tipo_usuario: str

class UsuarioUpdate(BaseModel):
    nome: str
    senha: str
    tipo_usuario: str

class CredenciaisLogin(BaseModel):
    email: str
    senha: str
