from fastapi import APIRouter, HTTPException,Depends, status
from model.model_usuario import UsuarioCreate, UsuarioUpdate, CredenciaisLogin
from controller.controller_usuario import UsuarioController
from datetime import datetime
from database.db_sqlite import SQLite
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from urllib.parse import unquote
from controller.token import Token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()


router = APIRouter()

#db = MySQL()
db = SQLite()
#db = MongoDB()
jwt_token = Token()
controller = UsuarioController(db)

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt_token.verificar_token(token)
        exp = payload.get('exp')
        if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expirado",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        return payload
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Erro inesperado ao verificar token: {e}") 
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar autenticação",
            headers={"WWW-Authenticate": "Bearer"},
        )


@router.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate):
    controller.criar_usuario(usuario)
    return {"message": "Usuário criado com sucesso"}

@router.get("/usuarios/", dependencies=[Depends(get_current_user)])
def listar_usuarios():
    return controller.listar_usuarios()

@router.put("/usuarios/{email}/", dependencies=[Depends(get_current_user)])
def editar_usuario(email: str, usuario: UsuarioUpdate):
    email_decoded = unquote(email)
    controller.editar_usuario_por_email(email_decoded, usuario)
    return {"message": "Usuário atualizado com sucesso"}

@router.delete("/usuarios/{email}/", dependencies=[Depends(get_current_user)])
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
            if '_id' in usuario and not isinstance(usuario['_id'], str):
                 usuario['_id'] = str(usuario['_id'])
            return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.post("/login/")
def login(credenciais: CredenciaisLogin):
    resultado = controller.login(credenciais.email, credenciais.senha)
    if resultado[0]:
        return {"message": "Login bem-sucedido", "token": resultado[1]}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")


