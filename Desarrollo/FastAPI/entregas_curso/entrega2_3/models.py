from pydantic import BaseModel, Field


class Partido(BaseModel):
    id: int
    anyo: int = Field(gt=1900, description="Año en que se disputó el partido. Se aceptan años desde el 1900")
    fase: str
    equipolocal: str
    goleslocales: int
    golesvisitante: int
    equipovisitante: str
    estaequipoanfitrion: int
