from fastapi import FastAPI
import json

# Carga de datos de prueba
file = open("datos/alimentos.json")
alimentos = json.load(file)

tags_metadata = [
    {
        "name" : "ingredientes",
        "description" : "Operaciones relacionadas con el CRUD de ingredientes." 
    }
]
# Objeto app de tipo FastAPI
app = FastAPI(
    title="FoodAPI",
    description="ApiRestFul para la gestión de alimentos y planes nutricionales",
    version="1.0",
    contact={
        "name" : "Facundo Brun",
        "url" : "https://github.com/facubrun"
    },
    license_info={
        "name" : "Apache 2.0",
        "url" : "https://apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=tags_metadata,
    )

# Configuracion del APIRestFUL

# Endpoint GET /
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Endpoint GET /ingredientes
@app.get("/ingredientes",tags=["ingredientes"])
async def read_ingredients():
    #await pedir datos
    return alimentos