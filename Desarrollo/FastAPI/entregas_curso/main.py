from fastapi import FastAPI, Response, status
import json
from carsdata import carsData

# Carga de datos de prueba
cars = carsData()


tags_metadata= {
        "name": "cars",
        "description": "Operaciones relacionadas con el CRUD de autos",
        },
# Objeto app de tipo FastAPI
app = FastAPI(
    title="CarsAPI",
    description="ApiRestFul para la gestión de autos",
    version="1.0",
    contact={
        "name" : "Facundo Brun",
        "url" : "https://github.com/facubrun"
    },
    license_info={
        "name" : "Apache 2.0",
        "url" : "https://apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=tags_metadata
    )

# Configuracion del APIRestFUL para autos

# Definición de los ENDPOINTS

# DEFAULT
@app.get("/")
async def read_root():
    return {"Hello": "World"}


# COCHES
@app.get("/cars",tags=["cars"])
async def read_cars(total:int=10,skip:int=0, todos:bool | None=None):
    #await pedir datos
    if(todos):
        return await cars.get_allCars()
    else:
        return await cars.get_cars(skip, total)

@app.get("/cars/{car_id}", tags=["cars"], status_code=status.HTTP_200_OK)
async def read_car(car_id: int, response: Response):
    # Buscamos el coche
    car = await cars.get_car(car_id)
    # Si encontramos coche, lo devolvemos
    if(car):
        return car
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error", str(car_id) + " no encontrado"}


@app.get("/brands", tags=["cars"], status_code=status.HTTP_200_OK)
async def read_cars_brand(brand_name: str, response: Response):
    # Buscamos coches para la marca dada
    brand_cars = await cars.get_carsBrand(brand_name)
    # Si encontramos lo devolvemos
    if brand_cars:
        return brand_cars
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"No se encontraron coches para la marca '{brand_name}'"}
