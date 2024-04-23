import mysql.connector
from mysql.connector import Error
from database.database_strategy import Database
from model.model_usuario import UsuarioCreate, UsuarioUpdate

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

    def criar_usuario(self, usuario_data: UsuarioCreate):
        query = """
        INSERT INTO usuarios (id, nome, senha, email) 
        VALUES (%s, %s, %s, %s);
        """
        vals = (usuario_data.id, usuario_data.nome, usuario_data.senha, usuario_data.email)
        self.execute_query(self.connection, query, vals)
        return usuario_data

    def listar_usuarios(self):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM usuarios;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result


    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        query = """
        UPDATE usuarios 
        SET nome = %s, senha = %s 
        WHERE email = %s;
        """
        vals = (usuario_data.nome, usuario_data.senha, email)
        self.execute_query(self.connection, query, vals)

    def excluir_usuario_por_email(self, email: str):
        query = "DELETE FROM usuarios WHERE email = %s;"
        vals = (email,)
        self.execute_query(self.connection, query, vals)

    def listar_usuario_por_email(self, email: str):
        query = "SELECT * FROM usuarios WHERE email = %s;"
        vals = (email,)
        return self.execute_query(self.connection, query, vals)

    def execute_query(self, connection, query, vals=None):
        cursor = connection.cursor()
        try:
            cursor.execute(query, vals)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")