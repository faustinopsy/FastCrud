from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime, timedelta
from datetime import datetime
import hashlib
from fastapi.security import HTTPBearer

security = HTTPBearer()

class Token:
    def __init__(self):
        self.secret_key = 'qwedfghhjkoi87555553dffdssss'
        self.algorithm = 'HS256'

    def verificar_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    def gerar_token(self, email: str, tipo_usuario: str) -> str:
        payload = {
            'email': email,
            'tipo_usuario': tipo_usuario,
            'iat': datetime.utcnow(), 
            'exp': datetime.utcnow() + timedelta(days=1)

        }
        jwt_token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return jwt_token
    
    async def get_current_user(self, credentials: HTTPAuthorizationCredentials = Depends(security)):
        token = credentials.credentials
        try:
            payload = self.verificar_token(token)
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
