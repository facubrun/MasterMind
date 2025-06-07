from api.data.fooddata import FoodData
from api.utilidades.models import Ingrediente, Plato, Usuario, UsuarioOut
from api.utilidades.docs import tags_metadata
from api.rutas.ingredientes import router as ingredientes_rutas
from api.rutas.platos import router as platos_rutas
from api.rutas.usuarios import router as usuarios_rutas
from api.main import app