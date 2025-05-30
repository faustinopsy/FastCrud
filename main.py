from fastapi import FastAPI
from router.routes_usuario import router as usuario_router
from router.routes_auth import router as routes_auth
from config.helper import add_cors

app = FastAPI()
app = FastAPI(debug=True)
add_cors(app)

app.include_router(usuario_router, tags=["usuarios"])
app.include_router(routes_auth, tags=["login"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
