# main.py

from fastapi import FastAPI, HTTPException
from model.models import UsuarioCreate, UsuarioUpdate
from controller.controllers import UsuarioController
from config.helper import add_cors

app = FastAPI()
controller = UsuarioController()

add_cors(app)

@app.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate):
    controller.criar_usuario(usuario)
    return {"message": "Usuário criado com sucesso"}

@app.get("/usuarios/")
def listar_usuarios():
    return controller.listar_usuarios()

@app.put("/usuarios/{email}/")
def editar_usuario(email: str, usuario: UsuarioUpdate):
    controller.editar_usuario_por_email(email, usuario)
    return {"message": "Usuário atualizado com sucesso"}

@app.delete("/usuarios/{email}/")
def excluir_usuario(email: str):
    controller.excluir_usuario_por_email(email)
    return {"message": "Usuário excluído com sucesso"}

@app.get("/usuarios/{email}/")
def listar_usuario_por_email(email: str):
    usuario = controller.listar_usuario_por_email(email)
    if usuario:
        usuario['_id'] = str(usuario['_id'])
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

