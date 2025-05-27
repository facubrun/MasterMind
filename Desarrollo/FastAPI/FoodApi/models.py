# Modelo Ingrediente
from enum import Enum
from pydantic import BaseModel


class TipoPlato(str, Enum):
    entrada = "entrada"
    principal = "principal"
    postre = "postre"
    bebida = "bebida"

# Modelo para la insercion de nuevos ingredientes
class Ingrediente(BaseModel):
    nombre: str
    calorias: int | None = None  # Opcional
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
    nombre: str
    tipo: TipoPlato
    ingredientes: list[IngredientePlato]
