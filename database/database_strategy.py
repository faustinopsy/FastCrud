from abc import ABC, abstractmethod
from mysql.connector import Error

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
