from pymongo import MongoClient
import hashlib
from database.database_strategy import Database

class MongoDB(Database):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['usuarios']
        self.collection = self.db['usuarios']

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def criar_usuario(self, usuario_data):
        usuario = usuario_data.dict()
        usuario['senha'] = self._hash_password(usuario['senha'])
        self.collection.insert_one(usuario)

    def login(self, email, senha):
        usuario = self.collection.find_one({'email': email})
        if usuario:
            if usuario['senha'] == self._hash_password(senha):
                return True
        return False

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
