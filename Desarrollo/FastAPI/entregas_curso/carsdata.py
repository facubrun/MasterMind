import json

# Clase que nos permite trabajar con datos de prueba

class carsData:


    def __init__(self):
        # Carga del fichero de datos de prueba
        self.fileCars=open('data/models.json')
        self.models = json.load(self.fileCars)
        self.fileCars.close()

    # INGREDIENTES
    # Devolución asincrona de datos de alimentos
    async def get_cars(self,skip,total):
        return { 'marcas' : self.models['marcas'][skip:(total + skip)]}
    
    async def get_allCars(self):
        return self.models

    # Devolución asincrona de un alimento
    async def get_car(self, car_id: int):

        # Inicializamos alimento como nulo
        car = None
        # Recorremos los datos del .json
        for item in self.models['marcas']:
            # Comparamos el id con el int que nos pasan
            if item['id'] == car_id:
                car = item
                break
        return car


    async def get_carsBrand(self, brand_name: str):
        brand_cars = []
        for item in self.models['marcas']:
            if item['marca'].lower() == brand_name.lower():
                car_id = item['id']
                car = await self.get_car(car_id)
                if car:
                    brand_cars.append(car)
        return brand_cars

