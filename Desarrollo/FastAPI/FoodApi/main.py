from typing import Annotated
from fastapi import Body, FastAPI, Response, status, Query, Path
import json
from models import Ingrediente, Plato
from fooddata import FoodData
from docs import tags_metadata

# Carga de datos de prueba
food = FoodData()
    
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

# Definición de los ENDPOINTS

# DEFAULT
@app.get("/")
async def read_root():
    return {"Hello": "World"}



# INGREDIENTES
@app.get("/ingredientes",tags=["ingredientes"])
async def read_ingredients(total:int,skip:int=0, todos:bool | None=None, filtronombre: Annotated[str | None, 
                        Query(min_length=3, max_length=10)] = None): # Si es path parameter, usamos annotated con Path 
                        #Si es query parameter, usamos annotated con Query
    #await pedir datos
    if(todos):
        return await food.get_allIngredientes()
    else:
        return await food.get_ingredientes(skip, total, filtronombre)

@app.get("/ingredientes/{ingrediente_id}", tags=["ingredientes"], status_code=status.HTTP_200_OK)
async def read_ingredient(ingrediente_id: Annotated[int | None, Path(ge=0)], 
                          response: Response):
    # Buscamos el ingrediente
    ingrediente = await food.get_ingrediente(ingrediente_id)
    # Si encontramos ingrediente, lo devolvemos
    if(ingrediente):
        return ingrediente
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(ingrediente_id) + " no encontrado"}


@app.post("/ingredientes", tags=["ingredientes"])
async def write_ingredients(ingrediente: Ingrediente):
    return await food.write_ingrediente(ingrediente)


@app.put("/ingredientes/{ingrediente_id}", tags=["ingredientes"])
async def update_ingredients(ingrediente_id: int, ingrediente : Ingrediente):
    return await food.update_ingrediente(ingrediente_id, ingrediente)


@app.delete("/ingredientes/{ingrediente_id}", tags=["ingredientes"])
async def delete_ingredients(ingrediente_id: int):
    return await food.delete_ingrediente(ingrediente_id)

@app.post("/ingredientes_platos", tags=["ingredientes"])
async def write_ingredients_platos(ingrediente: Ingrediente, plato: Plato):
    return await food.write_ingrediente_plato(ingrediente, plato)



# PLATOS
@app.get("/platos",tags=["platos"])
async def read_platos(total:int,skip:int=0, todos:bool | None=None):
    #await pedir datos
    if(todos):
        return await food.get_allPlatos()
    else:
        return await food.get_platos(skip, total)

@app.get("/platos/{plato_id}", tags=["platos"], status_code=status.HTTP_200_OK)
async def read_plato(plato_id: int, response: Response):
    # Buscamos el plato
    plato = await food.get_plato(plato_id)
    # Si encontramos plato, lo devolvemos
    if(plato):
        return plato
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(plato_id) + " no encontrado"}
    

@app.get("/platos/{plato_id}/ingredientes/{ingrediente_id}", tags=["platos"], status_code=status.HTTP_200_OK)
async def read_plato_ingrediente(plato_id: int, ingrediente_id:int, response: Response):
    # Buscamos ingrediente en el plato
    ingrediente = await food.get_ingredientePlato(plato_id, ingrediente_id)
    # Si encontramos lo devolvemos
    if(ingrediente):
        return ingrediente
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", "plato "+ str(plato_id) + ", ingrediente " + str(ingrediente_id) + " no encontrado"}
    

@app.post("/platos", tags=["platos"])
async def write_platos(plato: Plato, tiempo_destacado : int = Body()):
    return await food.write_plato(plato, tiempo_destacado)