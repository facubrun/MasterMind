#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from enum import Enum
from pydantic import BaseModel, Field


class tiposOS(str, Enum):
    windows = "windows"
    dos = "dos"
    ubuntu = "ubuntu"
    chrome = "chrome"
    mac = "mac"
    android = "android"
    otro = "otro"

# Modelo para un Laptop
class Portatil(BaseModel):
    modelo: str = Field(min_length=3, max_length=28, description="Modelo del portatil, entre 3 y 28 caracteres")
    precio : int = Field(gt=0, description="Precio del portatil, debe ser mayor que 0")
    memoriaram: int = Field(gt=0, le=128, description="Memoria RAM en GB, entre 0 y 128")
    OS : tiposOS = Field(default=tiposOS.otro, description="Sistema Operativo del portatil")
    anyosgarantia: int = Field(ge=0, le=5, description="Años de garantía, entre 0 y 5")

