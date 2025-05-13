import json

from models import Ingrediente, Plato

# Clase que nos permite trabajar con datos de prueba

class FoodData:

    alimentos= []
    platos= []
    destacados = []
    fileAlimentos = None
    filePlatos = None
    fileDestacados = None

    def __init__(self):
        # Carga del fichero de datos de prueba
        self.fileAlimentos=open('data/alimentos.json')
        self.alimentos = json.load(self.fileAlimentos)
        self.fileAlimentos.close()
        self.filePlatos=open('data/platos.json')
        self.platos = json.load(self.filePlatos)
        self.filePlatos.close()
        self.fileDestacados=open('data/destacados.json')
        self.destacados = json.load(self.fileDestacados)
        self.fileDestacados.close()

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
    

    # Recibimos y guardamos un nuevo ingrediente
    async def write_ingrediente(self, ingrediente: Ingrediente):
        self.fileAlimentos = open('data/alimentos.json','w')
        #Conseguimos el último id de la lista
        ultimo_alimento = self.alimentos['alimentos'][-1]['id']
        #Añadimos un nuevo id al ingrediente nuevo
        ingredienteDict = ingrediente.model_dump()
        ingredienteDict['id'] = ultimo_alimento + 1
        self.alimentos['alimentos'].append(ingredienteDict)
        json.dump(self.alimentos,self.fileAlimentos,indent=2)
        self.fileAlimentos.close()
        return ingredienteDict
    
    async def update_ingrediente(self, ingrediente_id: int, ingrediente: Ingrediente):
        self.fileAlimentos = open('data/alimentos.json', 'w')
        # Buscamos el ingrediente
        ingrediente_encontrado = None
        ingrediente_pos = 0
        # Recorremos los datos json
        for item in self.alimentos['alimentos']:
            # Comparamos ids
            if (item['id'] == ingrediente_id):
                ingrediente_encontrado = item
                break
            ingrediente_pos += 1

        # Si se encontró el ing
        if(ingrediente_encontrado):
            # Actualizamos
            ingredienteDict = ingrediente.model_dump()
            for elem in ingredienteDict:
                if(ingredienteDict[elem]):
                #cambiamos el valor
                    self.alimentos['alimentos'][ingrediente_pos][elem] = ingredienteDict[elem]
            json.dump(self.alimentos,self.fileAlimentos,indent=2)
            self.fileAlimentos.close()
            return self.alimentos['alimentos'][ingrediente_pos]
        else:
            return None
        
    async def delete_ingrediente(self,ingrediente_id):
        self.fileAlimentos = open('data/alimentos.json', 'w')
        # Buscamos el ingrediente
        ingrediente_encontrado = None
        ingrediente_pos = 0
        # Recorremos los datos json
        for item in self.alimentos['alimentos']:
            # Comparamos ids
            if (item['id'] == ingrediente_id):
                ingrediente_encontrado = item
                break
            ingrediente_pos += 1

        # Si se encontró el ing
        if(ingrediente_encontrado):
            # Eliminamos el inigrediente
            self.alimentos['alimentos'].pop(ingrediente_pos)
            json.dump(self.alimentos,self.fileAlimentos,indent=2)
            self.fileAlimentos.close()
            return {"info" : "ingrediente " + str(ingrediente_id) + "borrado correctamente."}
        else:
            return None

    async def write_ingrediente_plato(self, ingrediente: Ingrediente, plato: Plato):
        ingrediente = await self.write_ingrediente(ingrediente)
        # Serializamos para añadir id
        platoDict = plato.model_dump()
        platoDict['ingredientes'][0]['id'] = ingrediente['id']
        plato_con_ingrediente_id = Plato.model_validate(platoDict)
        platoDict = await self.write_plato(plato_con_ingrediente_id)
        return dict([('ingrediente', ingrediente),('plato', platoDict)])

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
    

# Recibimos y guardamos un nuevo plato
    async def write_plato(self, plato: Plato, tiempoDestacado: int):
        self.filePlatos = open('data/platos.json','w')
        #Conseguimos el último id de la lista
        ultimo_plato = self.platos['platos'][-1]['id']
        #Añadimos un nuevo id al plato nuevo
        platoDict = plato.model_dump()
        platoDict['id'] = ultimo_plato + 1
        self.platos['platos'].append(platoDict)
        json.dump(self.platos,self.filePlatos,indent=2)
        # Añadimos a destacado
        destacadoDict = await self.write_destacado(platoDict, tiempoDestacado)
        self.filePlatos.close()
        return platoDict
    
# DESTACADOS

# Añadimos un nuevo plato destacado
    async def write_destacado(self, plato: Plato, tiempo_destacado:int):
        self.fileDestacados=open('data/destacados.json','w')
        #Conseguimos el último id de la lista
        ultimo_destacado = self.destacados['destacados'][-1]['id']
        #Añadimos un nuevo destacado
        destacadoDict = {}
        destacadoDict['id']=ultimo_destacado + 1
        destacadoDict['id_plato'] = plato['id']
        destacadoDict['tiempo'] = tiempo_destacado
        self.destacados['destacados'].append(destacadoDict)
        json.dump(self.destacados,self.fileDestacados,indent=2)
        self.fileDestacados.close()
        return destacadoDict