import pytest
from fastapi.testclient import TestClient
from main import app  
from model.model_usuario import UsuarioCreate, UsuarioUpdate

client = TestClient(app)

def test_verificar_token_valido():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZHJpZ29AMTIzIiwiZXhwIjoxNzE3MDIxMTgyfQ.ohp51FchAKRhlHxXKtudZJyBxF77NHyZvNeEw7WOI3A"  
    response = client.get(f"/usuarios/verificar-token/?token={token}")
    assert response.status_code == 200
    assert response.json() == {"message": "Token válido"}

def test_verificar_token_expirado():
    token = "token_expirado_aqui"  
    response = client.get(f"/usuarios/verificar-token/?token={token}")
    assert response.status_code == 401
    assert response.json() == {"detail": "Token expirado"}

def test_verificar_token_invalido():
    token = "token_invalido_aqui"  
    response = client.get(f"/usuarios/verificar-token/?token={token}")
    assert response.status_code == 401
    assert response.json() == {"detail": "Token inválido"}

def test_criar_usuario():
    usuario = {"nome": "Teste", "email": "teste@example.com", "senha": "senha123"}
    response = client.post("/usuarios/usuarios/", json=usuario)
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário criado com sucesso"}

def test_listar_usuarios():
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InJvZHJpZ29AMTIzIiwiZXhwIjoxNzE3MDIxMTgyfQ.ohp51FchAKRhlHxXKtudZJyBxF77NHyZvNeEw7WOI3A" 
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/usuarios/usuarios/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_editar_usuario():
    email = "rodrigo@123"  
    usuario = {"nome": "Teste Atualizado", "senha": "nova_senha123"}
    response = client.put(f"/usuarios/usuarios/{email}/", json=usuario)
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário atualizado com sucesso"}


def test_excluir_usuario():
    email = "rodrigo@123" 
    response = client.delete(f"/usuarios/usuarios/{email}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Usuário excluído com sucesso"}


def test_listar_usuario_por_email():
    email = "rodrigo@123"  
    response = client.get(f"/usuarios/usuarios/{email}/")
    if response.status_code == 200:
        assert "email" in response.json()
    else:
        assert response.status_code == 404
        assert response.json() == {"detail": "Usuário não encontrado"}


def test_login():
    email = "rodrigo@123"  
    senha = "rodrigo@123"
    response = client.post(f"/usuarios/login/?email={email}&senha={senha}")
    if response.status_code == 200:
        assert "token" in response.json()
    else:
        assert response.status_code == 401
        assert response.json() == {"detail": "Credenciais inválidas"}
