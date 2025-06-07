from fastapi import FastAPI
from fastapi.testclient import TestClient
from api import app


# Cliente que utiliza la aplicación principal
client = TestClient(app)


# Primer test sobre el endpoint raiz
def test_read_default():
    response = client.get("/")
    assert response.status_code == 200 # assert <-> comprueba
    assert response.json() == {"Hello": "World"}

def test_read_ingrediente_id():
    response = client.get("/ingredientes/23")
    assert response.status_code == 200

def test_read_ingrediente_id_NO_encontrado():
    response = client.get("/ingredientes/23456789")
    assert response.status_code == 404
    assert response.json() == {"error": "Ingrediente con id 23456789 no encontrado"} # -> comprobamos que dicho id no es valido y da error

def test_create_ingrediente():
    response = client.post(
        "/ingredientes",
        headers={"Content-type": "application/json"},
        json={
            "nombre": "Prueba",
            "calorias": 20,
            "carbohidratos": 4.0,
            "proteinas": 1.0,
            "grasas": 0.2,
            "fibra": 1.5
        }
    )
    assert response.status_code == 200