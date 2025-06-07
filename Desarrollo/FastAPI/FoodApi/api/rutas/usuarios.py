from fastapi import APIRouter, BackgroundTasks
from typing import Annotated, Any
from api import Usuario,UsuarioOut
from api import FoodData

food = FoodData()
router = APIRouter()

def enviar_correo_fake(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@router.post("", response_model=UsuarioOut)
async def write_usuarios(usuario: Usuario, background_tasks: BackgroundTasks) -> Any:
    # tareas en segundo plano
    background_tasks.add_task(enviar_correo_fake, "facu@facu.uy", message="fake correo")
    return await food.write_usuario(usuario)