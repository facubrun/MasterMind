from api import PortatilData
from api import Portatil
from fastapi import APIRouter
from typing import Annotated
from fastapi import  HTTPException, Response, status, Query, Path


laptop = PortatilData()
router = APIRouter()

@router.get("/{portatil_id}", status_code=status.HTTP_200_OK, summary="Buscar un portatil",
            description="Buscar portatil a través del id")
async def get_portatil(portatil_id: Annotated[int | None, Path(description="id entero de busqueda", gt=0)], response: Response):
    # Buscamos el portatil
    portatil = await laptop.get_portatil(portatil_id)
    # Si encontramos portatil, lo devolvemos
    if(not portatil):
        raise HTTPException(
            status_code= 404,
            detail="Portatil con id " + str(portatil_id) + " no encontrado"
        )
    return portatil

@router.get("/filtro", status_code=status.HTTP_200_OK, summary="Buscar varios portatiles", 
            description="Buscar varios portatiles a través de un filtro de busqueda")
async def get_portatiles(total: Annotated[int, Query(description="Total de portatiles a devolver",)],
                           skip: int=0, 
                           filtronombre: Annotated[str | None, 
                                                Query(description="Filtro de busqueda por nombre",
                                                    min_length=3,
                                                    max_length=10)] = None): 
                        # Si es path parameter, usamos annotated con Path 
                        # Si es query parameter, usamos annotated con Query
    #await pedir datos
        return await laptop.get_portatiles(skip, total, filtronombre)

@router.get("", status_code=status.HTTP_200_OK, summary="Obtener todos los portatiles", 
            description="Obtener todos los portatiles guardados")
async def get_all_portatiles(): 
    #await pedir datos
        return await laptop.get_allPortatiles()

@router.get("/modelo", status_code=status.HTTP_200_OK, summary="Buscar portatiles por modelo",
            description="Buscar portatiles a través del modelo")
async def get_portatiles_modelo(skip: int, 
                                total: Annotated[int, Query(description="Total de portatiles del modelo elegido a devolver",)],
                           filtronombre: Annotated[str | None, 
                                                Query(description="Filtro de busqueda por nombre de modelo",
                                                    min_length=2,
                                                    max_length=28)] = None): 
    #await pedir datos
        return await laptop.get_portatilesModelo(skip, total, filtronombre)

@router.get("/precio", status_code=status.HTTP_200_OK, summary="Buscar portatiles por precio",
            description="Buscar portatiles filtrando por precio máximo")
async def get_portatiles_precioMax(precio: Annotated[int, Query(description="precio máximo de portatiles a devolver", gt=0)]): 
    #await pedir datos
        return await laptop.get_portatilesPrecioMax(precio)

@router.get("/os", status_code=status.HTTP_200_OK, summary="Buscar portatiles por sistema operativo",
            description="Buscar portatiles filtrando por sistema operativo")
async def get_portatiles_OS(os: Annotated[str, Query(description="nombre del sistema operativo del portatil", min_length=2, max_length=10)]): 
    #await pedir datos
        return await laptop.get_portatilesOS(os)

@router.post("", status_code=status.HTTP_201_CREATED, summary="Crear un nuevo portatil",
            description="Crear un nuevo portatil y guardarlo en el sistema")
async def write_portatil(portatil: Portatil):
    return await laptop.write_portatil(portatil)


@router.put("/{portatil_id}", status_code=status.HTTP_200_OK, summary="Actualizar un portatil",
            description="Actualizar un portatil existente a través de su id")
async def update_portatiles(portatil_id: int, portatil : Portatil):
    return await laptop.update_portatil(portatil_id, portatil)


@router.delete("/{portatil_id}", status_code=status.HTTP_200_OK, summary="Eliminar un portatil",
            description="Eliminar un portatil existente a través de su id")
async def delete_portatiles(portatil_id: int):
    return await laptop.delete_portatil(portatil_id)