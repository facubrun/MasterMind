# Modelo Ingrediente
from enum import Enum
from pydantic import BaseModel, Field


class TipoPlato(str, Enum):
    entrada = "entrada"
    principal = "principal"
    postre = "postre"
    bebida = "bebida"

# Modelo para la insercion de nuevos ingredientes
class Ingrediente(BaseModel):
    nombre: str
    calorias: int | None = Field(default=None, gt=0, description="Calorias del ingrediente. Entero mayor que 0")# Opcional
    carbohidratos: float | None = None
    proteinas: float | None = None
    grasas: float | None = None
    fibra: float | None = None

# Modelo para la insercion de nuevo plato

class IngredientePlato(BaseModel):
    id : int
    cant : int
    ud: str

class Plato(BaseModel):
    nombre: str = Field(description="Nombre del plato", max_length=128)
    tipo: TipoPlato
    ingredientes: list[IngredientePlato]

class Usuario(BaseModel):
    nombre: str 
    apellidos: str
    email: str
    password: str

class UsuarioOut(BaseModel): # Modelo para la salida de usuario sin password
    nombre: str
    apellidos: str
    email: str
