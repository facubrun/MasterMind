# Modelo Ingrediente
from pydantic import BaseModel


class Ingrediente(BaseModel):
    nombre: str
    calorias: int | None = None  # Opcional
    carbohidratos: float | None = None
    proteinas: float | None = None
    grasas: float | None = None
    fibra: float | None = None