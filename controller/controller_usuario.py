from model.model_usuario import UsuarioCreate, UsuarioUpdate
from database.database_strategy import Database
import hashlib
from controller.token import Token
from datetime import datetime, timedelta

class UsuarioController:
    def __init__(self, database: Database):
        self.db = database

    def criar_usuario(self, usuario_data: UsuarioCreate):
        self.db.criar_usuario(usuario_data)

    def listar_usuarios(self):
        return self.db.listar_usuarios()

    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        self.db.editar_usuario_por_email(email, usuario_data)

    def excluir_usuario_por_email(self, email: str):
        self.db.excluir_usuario_por_email(email)

    def listar_usuario_por_email(self, email: str):
        return self.db.listar_usuario_por_email(email)
    
    def login(self, email: str, senha: str) -> bool:
        jwt_token = Token()  
        usuario = self.listar_usuario_por_email(email)
        if usuario:
            senha_armazenada = usuario.get('senha')
            senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
            if senha_armazenada == senha_criptografada:
                jwt = jwt_token.gerar_token(email) 
                return [True ,jwt]
        return False
