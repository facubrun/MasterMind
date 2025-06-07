from fastapi import APIRouter
from fastapi import Body, HTTPException, Response, status
from starlette.exceptions import HTTPException as StarletteHTTPException
from api import Plato
from api import FoodData

food = FoodData()

router = APIRouter()

# PLATOS
@router.get("")
async def read_platos(total:int,skip:int=0, todos:bool | None=None):
    #await pedir datos
    if(todos):
        return await food.get_allPlatos()
    else:
        return await food.get_platos(skip, total)

@router.get("/{plato_id}", status_code=status.HTTP_200_OK)
async def read_plato(plato_id: int, response: Response):
    # Buscamos el plato
    plato = await food.get_plato(plato_id)
    # Si encontramos plato, lo devolvemos
    if(not plato):
        raise HTTPException(
            status_code= 404,
            detail="Plato con id " + str(plato_id) + " no encontrado"
        )
    return plato
    

@router.get("/{plato_id}/ingredientes/{ingrediente_id}", status_code=status.HTTP_200_OK)
async def read_plato_ingrediente(plato_id: int, ingrediente_id:int, response: Response):
    # Buscamos ingrediente en el plato
    ingrediente = await food.get_ingredientePlato(plato_id, ingrediente_id)
    # Si encontramos lo devolvemos
    if(ingrediente):
        return ingrediente
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", "plato "+ str(plato_id) + ", ingrediente " + str(ingrediente_id) + " no encontrado"}
    

@router.post("")
async def write_platos(plato: Plato, tiempo_destacado : int = Body()):
    return await food.write_plato(plato, tiempo_destacado)
