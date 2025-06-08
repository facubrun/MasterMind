from api.utilidades.models import Portatil
from api.data.portatildata import PortatilData
from api.rutas.portatiles import router as portatiles_rutas
from api.utilidades.docs import tags_metadata
from api.main import app

__all__ = ["Portatil", "PortatilData", "portatiles_rutas", "tags_metadata", "app"]