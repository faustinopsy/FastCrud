from model.model_usuario import UsuarioCreate, UsuarioUpdate
from database.database_strategy import Database

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