from pymongo import MongoClient
from database.database_strategy import Database

class MongoDB(Database):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['usuarios']
        self.collection = self.db['usuarios']

    def criar_usuario(self, usuario_data):
        usuario = usuario_data.dict()
        self.collection.insert_one(usuario)

    def listar_usuarios(self):
        usuarios = list(self.collection.find())
        for usuario in usuarios:
            usuario['_id'] = str(usuario['_id'])
        return usuarios

    def editar_usuario_por_email(self, email, usuario_data):
        novo_usuario = usuario_data.dict()
        self.collection.update_one({'email': email}, {'$set': novo_usuario})

    def excluir_usuario_por_email(self, email):
        self.collection.delete_one({'email': email})

    def listar_usuario_por_email(self, email):
        usuario = self.collection.find_one({'email': email})
        return usuario
