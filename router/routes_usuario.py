from fastapi import APIRouter, HTTPException,Depends, status
from model.model_usuario import UsuarioCreate, UsuarioUpdate
from controller.controller_usuario import UsuarioController
from datetime import datetime
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from urllib.parse import unquote
from controller.token import Token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


router = APIRouter()

db = MySQL()
#db = MongoDB()
jwt_token = Token()
controller = UsuarioController(db)


@router.get("/verificar-token/")
def verificar_token(token: str):
    try:
        payload = jwt_token.verificar_token(token) 
        exp = payload.get('exp')
        if exp:
            exp_date = datetime.fromtimestamp(exp)
            if exp_date > datetime.utcnow():
                return {"message": "Token válido"}
            else:
                raise HTTPException(status_code=401, detail="Token expirado")
        else:
            raise HTTPException(status_code=401, detail="Token inválido")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao verificar token")


@router.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate):
    controller.criar_usuario(usuario)
    return {"message": "Usuário criado com sucesso"}

@router.get("/usuarios/", dependencies=[Depends(verificar_token)])
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
    resultado = controller.login(email_decoded, senha)
    print(resultado)
    if resultado[0]:
        return {"message": "Login bem-sucedido","token" : resultado[1]}
    else:
        return {"status_code": 401,"detail" : "Credenciais inválidas"}
        #raise HTTPException(status_code=401, detail="Credenciais inválidas")