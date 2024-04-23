from model.models import UsuarioCreate, UsuarioUpdate
from database.db import Database

class UsuarioController:
    def __init__(self):
        self.db = Database()

    def criar_usuario(self, usuario_data: UsuarioCreate):
        usuario = usuario_data.dict()
        self.db.collection.insert_one(usuario)

    def listar_usuarios(self):
        usuarios = list(self.db.collection.find())
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
        return usuarios

    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        novo_usuario = usuario_data.dict()
        self.db.collection.update_one({'email': email}, {'$set': novo_usuario})

    def excluir_usuario_por_email(self, email: str):
        self.db.collection.delete_one({'email': email})

    def listar_usuario_por_email(self, email: str):
        usuario = self.db.collection.find_one({'email': email})
        return usuario
