from abc import ABC, abstractmethod
from mysql.connector import Error
from typing import List
from datetime import datetime

class Database(ABC):

    @abstractmethod
    def criar_usuario(self, usuario_data):
        pass

    @abstractmethod
    def listar_usuarios(self):
        pass

    @abstractmethod
    def editar_usuario_por_email(self, email, usuario_data):
        pass

    @abstractmethod
    def excluir_usuario_por_email(self, email):
        pass

    @abstractmethod
    def listar_usuario_por_email(self, email):
        pass

    @abstractmethod
    def inserir_acesso(self, acesso_data: dict):
        pass

    @abstractmethod
    def listar_acessos(self) -> List[dict]:
        pass

    @abstractmethod
    def consultar_acessos_por_metodo(self, method: str) -> List[dict]:
        pass

    @abstractmethod
    def consultar_acessos_por_data(self, start_date: datetime, end_date: datetime) -> List[dict]:
        pass