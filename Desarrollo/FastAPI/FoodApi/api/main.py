from fastapi import FastAPI
import uvicorn
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from api import FoodData, platos_rutas, ingredientes_rutas, usuarios_rutas
from api import tags_metadata
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
app.include_router(ingredientes_rutas,
                   tags=["ingredientes"],
                   prefix="/ingredientes")

# PLATOS
app.include_router(platos_rutas,
                   tags=["platos"],
                   prefix="/platos")

# USUARIOS
app.include_router(usuarios_rutas,
                   tags=["usuarios"],
                   prefix="/usuarios")

# DEBBUGGING
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)