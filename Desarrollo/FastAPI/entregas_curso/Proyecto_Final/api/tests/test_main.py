from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app


# Cliente que utiliza la aplicación principal
client = TestClient(app)

def test_get_portatil_id():
    response = client.get("/portatiles/3")
    assert response.status_code == 200

def test_get_all_portatiles():
    response = client.get("/portatiles/")
    assert response.status_code == 200

def test_get_portatil_id_NO_encontrado():
    response = client.get("/portatiles/23456789")
    assert response.status_code == 404
    assert response.json() == {"error": "Portatil con id 23456789 no encontrado"} # -> comprobamos que dicho id no es valido y da error

def test_create_ingrediente():
    response = client.post(
        "/portatiles",
        headers={"Content-type": "application/json"},
        json={
            "modelo": "Lenovo ThinkPad X1 Carbon",
            "precio": 1500,
            "memoriaram":  "16",
            "OS": "windows",
            "anyosgarantia": 3
        }
    )
    assert response.status_code == 201

def test_delete_ingrediente():
    response = client.delete("/portatiles/234")
    assert response.status_code == 200