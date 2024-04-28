import mysql.connector
from mysql.connector import Error
from database.database_strategy import Database
from model.model_usuario import UsuarioCreate, UsuarioUpdate
import hashlib
import uuid
from typing import List
from datetime import datetime

class MySQL(Database):
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "root"
        self.database = "fastcrud"
        self.connection = self.create_server_connection()

    def create_server_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            print("MySQL Database connection successful")
            return connection
        except Error as err:
            print(f"Error: '{err}'")
    
    def execute_query(self, connection, query, vals=None):
        cursor = connection.cursor()
        try:
            cursor.execute(query, vals)
            connection.commit()
            print("Query successful")
            for _ in cursor:
                pass
        except Error as err:
            print(f"Error: '{err}'")

    def criar_usuario(self, usuario_data: UsuarioCreate):
        usuario_data.id = str(uuid.uuid4())
        senha_criptografada = self.criptografar_senha(usuario_data.senha)
        query = """
        INSERT INTO usuarios (id, nome, senha, email) 
        VALUES (%s, %s, %s, %s);
        """
        vals = (usuario_data.id, usuario_data.nome, senha_criptografada, usuario_data.email)
        self.execute_query(self.connection, query, vals)
        return usuario_data

    def login(self, email: str, senha: str) -> bool:
        query = "SELECT senha FROM usuarios WHERE email = %s;"
        vals = (email,)
        cursor = self.connection.cursor()
        cursor.execute(query, vals)
        senha_armazenada = cursor.fetchone()
        if senha_armazenada:
            senha_armazenada = senha_armazenada[0]
            senha_criptografada = self.criptografar_senha(senha)
            return senha_armazenada == senha_criptografada
        return False

    def criptografar_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    def listar_usuarios(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM usuarios;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        senha_criptografada = self.criptografar_senha(usuario_data.senha)
        print("Editando usuário por email:", email)
        query = """
        UPDATE usuarios 
        SET nome = %s, senha = %s 
        WHERE email = %s;
        """
        vals = (usuario_data.nome, senha_criptografada, email)
        self.execute_query(self.connection, query, vals)

    def excluir_usuario_por_email(self, email: str):
        print("Excluindo usuário por email:", email)
        query = "DELETE FROM usuarios WHERE email = %s;"
        vals = (email,)
        self.execute_query(self.connection, query, vals)

    def listar_usuario_por_email(self, email: str):
        cursor = self.connection.cursor(dictionary=True)
        print("Listando usuário por email:", email)
        query = "SELECT * FROM usuarios WHERE email = %s;"
        vals = (email,)
        cursor.execute(query,vals)
        result = cursor.fetchone()
        return result
        #return self.execute_query(self.connection, query, vals)

    def inserir_acesso(self, acesso_data):
        acesso_data['id']= str(uuid.uuid4())
        query = """
        INSERT INTO logs (id,path, client_ip, method, data_ini, data_fim, process_time) 
        VALUES (%s,%s, %s, %s, %s, %s, %s);
        """
        vals = (
            acesso_data['id'],
            acesso_data['path'],
            acesso_data['client_ip'],
            acesso_data['method'],
            acesso_data['data_ini'],
            acesso_data['data_fim'],
            acesso_data['process_time']
        )
        self.execute_query(self.connection, query, vals)

    def listar_acessos(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM logs;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def consultar_acessos_por_metodo(self, method: str):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM logs WHERE method = %s;"
        vals = (method,)
        cursor.execute(query, vals)
        result = cursor.fetchall()
        return result

    def consultar_acessos_por_data(self, data_ini: datetime, data_fim: datetime):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM logs WHERE data_ini BETWEEN %s AND %s;"
        vals = (data_ini, data_fim)
        cursor.execute(query, vals)
        result = cursor.fetchall()
        return result