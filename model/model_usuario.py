from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    id: str 
    nome: str
    senha: str
    email: str

class UsuarioUpdate(BaseModel):
    nome: str
    senha: str
