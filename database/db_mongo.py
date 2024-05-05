from pymongo import MongoClient
import hashlib
from database.database_strategy import Database
import uuid
from typing import List
from datetime import datetime

class MongoDB(Database):
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['usuarios']
        self.collection = self.db['usuarios']

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def criar_usuario(self, usuario_data):
        usuario_data.id = str(uuid.uuid4())
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
        novo_usuario['senha'] = self._hash_password(novo_usuario['senha'])
        self.collection.update_one({'email': email}, {'$set': novo_usuario})

    def excluir_usuario_por_email(self, email):
        self.collection.delete_one({'email': email})

    def listar_usuario_por_email(self, email):
        usuario = self.collection.find_one({'email': email})
        return usuario

    def inserir_acesso(self, acesso_data):
        acesso_data.id = str(uuid.uuid4())
        self.collection.insert_one(acesso_data)

    def listar_acessos(self):
        return list(self.collection.find())

    def consultar_acessos_por_metodo(self, method: str):
        logs = self.collection.find({"method": method})
        return logs

    def consultar_acessos_por_data(self, data_ini: datetime, data_fim: datetime):
        return self.collection.find({
            "data_ini": {"$gte": data_ini},
            "data_fim": {"$lte": data_fim}
        })