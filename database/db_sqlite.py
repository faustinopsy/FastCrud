import sqlite3
from database.database_strategy import Database
from model.model_usuario import UsuarioCreate, UsuarioUpdate
import hashlib
import uuid

class SQLite(Database):
    def __init__(self):
        self.db_path = "./usuarios.db"
        self.criar_tabela_usuarios()

    def get_connection(self):
        connection = sqlite3.connect(self.db_path, check_same_thread=False)
        connection.row_factory = sqlite3.Row
        return connection

    def criptografar_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    def execute_query(self, query, vals=None):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if vals:
                cursor.execute(query, vals)
            else:
                cursor.execute(query)
            conn.commit()
        except sqlite3.Error as err:
            print(f"SQLite Error: {err}")
            return None
        finally:
            conn.close()

    def fetch_query(self, query, vals=None):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if vals:
                cursor.execute(query, vals)
            else:
                cursor.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as err:
            print(f"SQLite Error: {err}")
            return None
        finally:
            conn.close()

    def fetch_one_query(self, query, vals=None):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if vals:
                cursor.execute(query, vals)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        except sqlite3.Error as err:
            print(f"SQLite Error: {err}")
            return None
        finally:
            conn.close()

    def criar_usuario(self, usuario_data: UsuarioCreate):
        usuario_data.id = str(uuid.uuid4())
        senha_criptografada = self.criptografar_senha(usuario_data.senha)
        query = """
        INSERT INTO usuarios (id, nome, senha, email, tipo_usuario) 
        VALUES (?, ?, ?, ?, ?);
        """
        vals = (usuario_data.id, usuario_data.nome, senha_criptografada, usuario_data.email, usuario_data.tipo_usuario)
        self.execute_query(query, vals)
        return usuario_data

    def listar_usuarios(self):
        query = "SELECT * FROM usuarios;"
        rows = self.fetch_query(query)
        if rows:
            return [dict(row) for row in rows]
        return []

    def editar_usuario_por_email(self, email: str, usuario_data: UsuarioUpdate):
        senha_criptografada = self.criptografar_senha(usuario_data.senha)
        query = """
        UPDATE usuarios 
        SET nome = ?, senha = ?, , tipo_usuario = ?
        WHERE email = ?;
        """
        vals = (usuario_data.nome, senha_criptografada, usuario_data.tipo_usuario, email)
        self.execute_query(query, vals)

    def excluir_usuario_por_email(self, email: str):
        query = "DELETE FROM usuarios WHERE email = ?;"
        vals = (email,)
        self.execute_query(query, vals)

    def listar_usuario_por_email(self, email: str):
        query = "SELECT * FROM usuarios WHERE email = ?;"
        vals = (email,)
        result = self.fetch_one_query(query, vals)
        return dict(result) if result else None

    def criar_tabela_usuarios(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    tipo_usuario TEXT NOT NULL
                );
            """)
            conn.commit()
            print("Tabela 'usuarios' criada com sucesso.")
        except sqlite3.Error as err:
            print(f"Erro SQLite: {err}")
        finally:
            conn.close()
