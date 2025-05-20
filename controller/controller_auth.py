from model.model_usuario import UsuarioCreate, UsuarioUpdate
from database.database_strategy import Database
from controller.token import Token
from datetime import datetime
import hashlib
import re
from fastapi import HTTPException

class UsuarioAuth:
    def __init__(self, database: Database):
        self.db = database

    def validar_email(self, email: str):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email)

    def login(self, email: str, senha: str):
        if not email or not senha:
            raise HTTPException(status_code=400, detail="Email e senha são obrigatórios.")

        if not self.validar_email(email):
            raise HTTPException(status_code=400, detail="Email inválido.")

        usuario = self.db.listar_usuario_por_email(email)
        if not usuario:
            raise HTTPException(status_code=401, detail="Credenciais inválidas.")

        senha_armazenada = usuario.get('senha')
        senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()

        if senha_armazenada == senha_criptografada:
            jwt_token = Token()
            jwt = jwt_token.gerar_token(email)
            return [True, jwt]
        
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
