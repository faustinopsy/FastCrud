from fastapi import APIRouter, HTTPException
from model.model_usuario import UsuarioCreate, UsuarioUpdate
from controller.controller_usuario import UsuarioController
from database.db_mysql import MySQL
from database.db_mongo import MongoDB

router = APIRouter()

db = MySQL()
#db = MongoDB()

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
    controller.editar_usuario_por_email(email, usuario)
    return {"message": "Usuário atualizado com sucesso"}

@router.delete("/usuarios/{email}/")
def excluir_usuario(email: str):
    controller.excluir_usuario_por_email(email)
    return {"message": "Usuário excluído com sucesso"}

@router.get("/usuarios/{email}/")
def listar_usuario_por_email(email: str):
    usuario = controller.listar_usuario_por_email(email)
    if usuario:
        usuario['_id'] = str(usuario['_id'])
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
