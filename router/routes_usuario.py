from fastapi import APIRouter, HTTPException
from model.model_usuario import UsuarioCreate, UsuarioUpdate
from controller.controller_usuario import UsuarioController
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from urllib.parse import unquote

router = APIRouter()

#db = MySQL()
db = MongoDB()

controller = UsuarioController(db)

@router.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate):
    controller.criar_usuario(usuario)
    return {"message": "Usuário criado com sucesso"}

@router.get("/usuarios/")
def listar_usuarios():
    return controller.listar_usuarios()

@router.put("/usuarios/{email}/")
def editar_usuario(email: str, usuario: UsuarioUpdate):
    email_decoded = unquote(email)
    controller.editar_usuario_por_email(email_decoded, usuario)
    return {"message": "Usuário atualizado com sucesso"}

@router.delete("/usuarios/{email}/")
def excluir_usuario(email: str):
    email_decoded = unquote(email)
    controller.excluir_usuario_por_email(email_decoded)
    return {"message": "Usuário excluído com sucesso"}

@router.get("/usuarios/{email}/")
def listar_usuario_por_email(email: str):
    email_decoded = unquote(email)
    usuario = controller.listar_usuario_por_email(email_decoded)
    if usuario:
        if isinstance(db, MySQL): 
            return usuario
        else:
            usuario['_id'] = str(usuario['_id'])
            return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.post("/login/")
def login(email: str, senha: str):
    email_decoded = unquote(email)
    if controller.login(email_decoded, senha):
        return {"message": "Login bem-sucedido"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")