from fastapi import FastAPI
from router.routes_usuario import router as usuario_router
from config.helper import add_cors

app = FastAPI()
app = FastAPI(debug=True)
add_cors(app)

app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
