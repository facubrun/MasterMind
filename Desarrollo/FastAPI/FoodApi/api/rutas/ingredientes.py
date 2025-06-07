from fastapi import APIRouter
from typing import Annotated
from fastapi import  HTTPException, Response, status, Query, Path
from api import Ingrediente, Plato
from api import FoodData

food = FoodData()
router = APIRouter()

@router.get("")
async def read_ingredients(total: Annotated[int, Query(description="Total de ingredientes a devolver",)],
                           skip: int=0, 
                           todos:bool | None=None,
                           filtronombre: Annotated[str | None, 
                                                Query(description="Filtro de busqueda por nombre",
                                                    min_length=3,
                                                    max_length=10)] = None): 
                        # Si es path parameter, usamos annotated con Path 
                        # Si es query parameter, usamos annotated con Query
    #await pedir datos
    if(todos):
        return await food.get_allIngredientes()
    else:
        return await food.get_ingredientes(skip, total, filtronombre)

@router.get("/{ingrediente_id}", status_code=status.HTTP_200_OK, summary="Buscar ingrediente",
            description="Buscar ingrediente a través del id")
async def read_ingredient(ingrediente_id: Annotated[int | None, Path(description="id entero de busqueda", ge=0)], response: Response):
    # Buscamos el ingrediente
    ingrediente = await food.get_ingrediente(ingrediente_id)
    # Si encontramos ingrediente, lo devolvemos
    if(not ingrediente):
        raise HTTPException(
            status_code= 404,
            detail="Ingrediente con id " + str(ingrediente_id) + " no encontrado"
        )
    return ingrediente


@router.post("")
async def write_ingredients(ingrediente: Ingrediente):
    return await food.write_ingrediente(ingrediente)


@router.put("/{ingrediente_id}")
async def update_ingredients(ingrediente_id: int, ingrediente : Ingrediente):
    return await food.update_ingrediente(ingrediente_id, ingrediente)


@router.delete("/{ingrediente_id}")
async def delete_ingredients(ingrediente_id: int):
    return await food.delete_ingrediente(ingrediente_id)

@router.post("/ingredientes_platos")
async def write_ingredients_platos(ingrediente: Ingrediente, plato: Plato):
    return await food.write_ingrediente_plato(ingrediente, plato)