from fastapi import FastAPI,Request
from router.routes_usuario import router as usuario_router
from router.routes_logs import router as routes_logs
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from service.cors import add_cors
from service.monitor import monitorar
from model.model_logs import Logs
from database.db_mysql import MySQL
from database.db_mongo import MongoDB
from controller.LogController import LogController
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True)


@app.middleware("http")
async def monitor(request: Request, call_next):
    return await monitorar(request, call_next)

add_cors(app)
app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(routes_logs, prefix="/logs", tags=["logs"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
