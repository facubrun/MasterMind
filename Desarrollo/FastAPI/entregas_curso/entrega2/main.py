from fastapi import Body, FastAPI, Path, Query, Response, status
import json
from models import Partido
from futboldata import FutbolData
from docs import tags_metadata
from typing import Annotated, Optional

# Carga de datos de prueba
futbol = FutbolData()
    
# Objeto app de tipo FastAPI
app = FastAPI(
    title="FutbolAPI",
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



# PARTIDOS
# 1. GET partidos devuelve un número de partidos marcado por el query parameter total comenzando en skip.
@app.get("/partidos",tags=["partidos"], summary="Devolver cierta cantidad de partidos",
            description="Devuelve un número de partidos marcado por el query parameter total comenzando en skip.")
async def read_partido(total: Annotated[int, Query(description="Total de ingredientes a devolver", gt=0)],
                        skip: Annotated[int, Query(description="A partir de que ingrediente se devuelve", gt=0)]):
    #await pedir datos
    return await futbol.get_partidos(skip, total)


# 2. GET todospartidos devuelve todos los partidos.
@app.get("/todospartidos",tags=["partidos"])
async def read_all_partidos():
    #await pedir datos
    return await futbol.get_allPartidos()


# 3. GET partidos/{partido_id} devuelve un partido en concreto.
@app.get("/partidos/{partido_id}", tags=["partidos"], status_code=status.HTTP_200_OK, summary="Devolver un partido por id",
            description="Devuelve un partido en concreto. El id del partido se envía por path.")
async def read_partido(partido_id: Annotated[int | None, Path(description="id entero de busqueda", gt=0)], response: Response):
    # Buscamos el partido
    partido = await futbol.get_partido(partido_id)
    # Si encontramos partido, lo devolvemos
    if(partido):
        return partido
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(partido_id) + " no encontrado"}


# 4. GET partidosequipo devuelve todos los partidos jugados por el equipo enviado, este parámetro se puede enviar por Path o Query parameter
@app.get("/partidos_equipo/{equipo_path}", tags=["partidos"])
@app.get("/partidos_equipo/", tags=["partidos"])  # Ruta sin path para usar solo query
async def partidos_equipo(response: Response,equipo_path: str | None = None ,equipo: str | None = None):
    equipo_nombre = equipo_path or equipo

    partido_equipo = await futbol.get_partidosEquipo(equipo_nombre)
    
    if (partido_equipo):
        return partido_equipo
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error:" + equipo_nombre + "no encontrado"}


#  5. POST partidos crea un nuevo partido.
@app.post("/partidos", tags=["partidos"], summary="Crear un nuevo partido",
            description="Crea un nuevo partido. El partido se envía en el body de la petición.")
async def write_partidos(partido: Partido):
    return await futbol.write_partido(partido)

@app.put("/partidos/{partido_id}", tags=["partidos"])
async def update_partidos(partido_id: int, partido : Partido):
    return await futbol.update_partido(partido_id, partido)

# 7. DELETE partidos borra un partido existente.
@app.delete("/partidos/{partido_id}", tags=["partidos"])
async def delete_partido(partido_id: int):
    return await futbol.delete_partido(partido_id)

