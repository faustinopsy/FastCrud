import mysql.connector
from mysql.connector import Error
from database.database_strategy import Database
from model.model_usuario import UsuarioCreate, UsuarioUpdate
import hashlib
import uuid

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
