from fastapi import FastAPI,Request
from router.routes_usuario import router as usuario_router
from router.routes_logs import router as routes_logs
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from config.helper import add_cors
from model.model_logs import Logs
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from controller.LogController import LogController
from datetime import datetime


app = FastAPI(debug=True)

add_cors(app)

@app.middleware("http")
async def monitorar(request: Request, call_next):
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


app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(routes_logs, prefix="/logs", tags=["logs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
