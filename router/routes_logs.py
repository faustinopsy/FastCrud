import asyncio
from typing import List
from fastapi import APIRouter, HTTPException,Depends, Request, Response
from model.model_logs import Logs
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from controller.LogController import LogController
from datetime import datetime
from urllib.parse import unquote
from controller.token import Token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import StreamingResponse
import json

router = APIRouter()
db = MySQL()
jwt_token = Token()
log_controller = LogController(db)  


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



@router.get("/acessos/")  
def consultar_acessos():
    acessos = log_controller.listar_acessos()
    return acessos

@router.get("/acessos/metodo/{metodo}")  
def consultar_acessos_por_metodo(metodo: str):
    acessos = log_controller.consultar_acessos_por_metodo(metodo)
    return acessos

@router.get("/acessos/data/{data_ini}/{data_fim}")  
def consultar_acessos_por_data(data_ini: str, data_fim: str):
    start_date = datetime.strptime(data_ini, "%Y-%m-%d")
    end_date = datetime.strptime(data_fim, "%Y-%m-%d")
    acessos = log_controller.consultar_acessos_por_data(start_date, end_date)
    return acessos

last_log_timestamp = None  

@router.get("/acessos/stream", dependencies=[Depends(verificar_token)])
async def stream_logs(response: Response):
    async def event_generator():
        global last_log_timestamp  
        while True:
            logs = log_controller.listar_acessos()  
            if logs:  
                logs_sorted = sorted(logs, key=lambda x: x["data_ini"])
                for log in logs_sorted:
                    log["data_ini"] = log["data_ini"].isoformat()
                    log["data_fim"] = log["data_fim"].isoformat()
                    yield f"data: {json.dumps(log)}\n\n"
                last_log_timestamp = logs_sorted[-1]["data_ini"]  
            await asyncio.sleep(10)

    return StreamingResponse(event_generator(), media_type="text/event-stream")