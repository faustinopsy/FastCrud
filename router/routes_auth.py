from fastapi import APIRouter, HTTPException
from model.model_usuario import CredenciaisLogin
from controller.controller_auth import UsuarioAuth
from database.db_sqlite import SQLite
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from urllib.parse import unquote



router = APIRouter()

#db = MySQL()
db = SQLite()
#db = MongoDB()

controller = UsuarioAuth(db)


@router.post("/login/")
def login(credenciais: CredenciaisLogin):
    resultado = controller.login(credenciais.email, credenciais.senha)
    if resultado[0]:
        return {"message": "Login bem-sucedido", "token": resultado[1]}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")


