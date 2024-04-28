from fastapi import Request, Response
from datetime import datetime
from database.db_mongo import MongoDB
from controller.LogController import LogController
from model.model_logs import Logs
from database.db_mysql import MySQL
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware

async def monitorar(request: Request, call_next):
    if request.url.path == "/logs/acessos/stream":
        return await call_next(request)
    data_ini = datetime.utcnow()
    path = request.url.path
    client_ip = request.client.host
    method = request.method

    #db = MongoDB()  
    db = MySQL()

    log_controller = LogController(db)
    response = await call_next(request)
    data_fim = datetime.utcnow()
    process_time = (data_fim - data_ini).microseconds / 1000

    data_ini_str = data_ini.isoformat()
    data_fim_str = data_fim.isoformat()

    log_entry = Logs(
        path=path,
        method=method,
        client_ip=client_ip,
        data_ini=data_ini_str,
        data_fim=data_fim_str,
        process_time=str(process_time)
    )

    acesso_data = log_entry.dict()
    log_controller.inserir_acesso(acesso_data)

    return response
