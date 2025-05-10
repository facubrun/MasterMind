import json

# Clase que nos permite trabajar con datos de prueba

class FoodData:

    alimentos=[]
    platos=[]

    def __init__(self):
        # Carga del fichero de datos de prueba
        self.fileAlimentos=open('data/alimentos.json')
        self.alimentos = json.load(self.fileAlimentos)
        self.fileAlimentos.close()
        self.filePlatos=open('data/platos.json')
        self.platos = json.load(self.filePlatos)
        self.filePlatos.close()

    # INGREDIENTES
    # Devolución asincrona de datos de alimentos
    async def get_ingredientes(self,skip,total):
        return { 'alimentos' : self.alimentos['alimentos'][skip:(total + skip)]}
    
    async def get_allIngredientes(self):
        return self.alimentos

    # Devolución asincrona de un alimento
    async def get_ingrediente(self, ingrediente_id: int):
        #alimento = {"error", str(ingrediente_id) + " no encontrado"}

        # Inicializamos alimento como nulo
        alimento = None
        # Recorremos los datos del .json
        for item in self.alimentos['alimentos']:
            # Comparamos el id con el int que nos pasan
            if item['id'] == ingrediente_id:
                alimento = item
                break
        return alimento
    

    #PLATOS    
    async def get_allPlatos(self):
        return self.platos

    # Devolucion asincrona de un alimento
    async def get_plato(self,plato_id: int):
        plato=None
        #Recorremos todos los datos JSON
        for item in self.platos['platos']:
            #Comparamos el id que es int
            if item['id']==plato_id:
                plato=item
                break
        return plato

    async def get_ingredientePlato(self,plato_id: int,ingrediente_id: int):
        plato=await self.get_plato(plato_id)
        ingrediente=None
        if(plato):
            for item in plato['ingredientes']:
                # Comparamos el id que es int
                if item['id'] == ingrediente_id:
                    ingrediente = await self.get_ingrediente(ingrediente_id)
                    break
        return ingrediente
