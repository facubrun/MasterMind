import uvicorn
from typing import Annotated, Any
from fastapi import Body, FastAPI, HTTPException, Response, status, Query, Path, BackgroundTasks
import json
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from models import Ingrediente, Plato, Usuario, UsuarioOut
from fooddata import FoodData
from docs import tags_metadata
from fastapi.responses import JSONResponse

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

# Manejo de excepciones

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code= exc.status_code,
        content={"error": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def http_exception_handler(request, exc):
    # Conversion a dict
    errorDict = eval(str(exc))

    # Manejamos diferentes codigos de error
    if errorDict[0]["type"] == "greater_than_or_equal":
        codigoError = 422
    else:
        codigoError = 404
    return JSONResponse(
        status_code= codigoError,
        content={
            "error": errorDict[0]["msg"], 
            "dato enviado": str(errorDict[0]["input"])
            },
    )


# Configuracion del APIRestFUL

# Definición de los ENDPOINTS

# DEFAULT
@app.get("/")
async def read_root():
    return {"Hello": "World"}



# INGREDIENTES
@app.get("/ingredientes",tags=["ingredientes"])
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

@app.get("/ingredientes/{ingrediente_id}", tags=["ingredientes"], status_code=status.HTTP_200_OK, summary="Buscar ingrediente",
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
    if(not plato):
        raise HTTPException(
            status_code= 404,
            detail="Plato con id " + str(plato_id) + " no encontrado"
        )
    return plato
    

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

# USUARIOS

def enviar_correo_fake(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/usuarios", tags=["usuarios"], response_model=UsuarioOut)
async def write_usuarios(usuario: Usuario, background_tasks: BackgroundTasks) -> Any:
    # tareas en segundo plano
    background_tasks.add_task(enviar_correo_fake, "facu@facu.uy", message="fake correo")
    return await food.write_usuario(usuario)

# DEBBUGGING
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)