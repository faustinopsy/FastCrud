from model.model_logs import Logs
from database.database_strategy import Database
from datetime import datetime
from typing import List  

class LogController:
    def __init__(self, database: Database):
        self.db = database

    def inserir_acesso(self, acesso_data: Logs):
        self.db.inserir_acesso(acesso_data)

    def listar_acessos(self):  
        return self.db.listar_acessos() 

    def consultar_acessos_por_metodo(self, method: str):  
        return self.db.consultar_acessos_por_metodo(method)

    def consultar_acessos_por_data(self, start_date: datetime, end_date: datetime):  
        return self.db.consultar_acessos_por_data(start_date, end_date)
