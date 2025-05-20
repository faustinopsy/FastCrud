from model.model_usuario import UsuarioCreate, UsuarioUpdate
from database.database_strategy import Database

import re
from fastapi import HTTPException

class UsuarioController:
    def __init__(self, database: Database):
        self.db = database

    def validar_email(self, email: str):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(regex, email)

    def criar_usuario(self, usuario_data: UsuarioCreate):
        if not usuario_data.nome or not usuario_data.email or not usuario_data.senha:
            raise HTTPException(status_code=400, detail="Todos os campos são obrigatórios.")

        if not self.validar_email(usuario_data.email):
            raise HTTPException(status_code=400, detail="Email inválido.")

        if len(usuario_data.senha) < 6:
            raise HTTPException(status_code=400, detail="A senha deve ter no mínimo 8 caracteres.")

        usuario_existente = self.db.listar_usuario_por_email(usuario_data.email)
        if usuario_existente:
            raise HTTPException(status_code=409, detail="Email já cadastrado.")
        
        return self.db.criar_usuario(usuario_data)

    def listar_usuarios(self):
        usuarios = self.db.listar_usuarios()
        if not usuarios:
            raise HTTPException(status_code=404, detail="Nenhum usuário encontrado.")
        return usuarios

    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        if not usuario_data.nome or not usuario_data.senha:
            raise HTTPException(status_code=400, detail="Nome e senha são obrigatórios.")
        
        if len(usuario_data.senha) < 6:
            raise HTTPException(status_code=400, detail="A senha deve ter no mínimo 8 caracteres.")
        
        usuario_existente = self.db.listar_usuario_por_email(email)
        if not usuario_existente:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        return self.db.editar_usuario_por_email(email, usuario_data)

    def excluir_usuario_por_email(self, email: str):
        usuario_existente = self.db.listar_usuario_por_email(email)
        if not usuario_existente:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        
        return self.db.excluir_usuario_por_email(email)

    def listar_usuario_por_email(self, email: str):
        usuario = self.db.listar_usuario_por_email(email)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        return usuario
    
