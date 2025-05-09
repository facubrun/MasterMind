from fastapi import FastAPI


tags_metadata = [
    {
        "name" : "courses",
        "description" : "Operaciones relacionadas con el CRUD de cursos." 
    }
]
# Objeto app de tipo FastAPI
app = FastAPI(
    title="CoursesAPI",
    description="API para gestionar avance de la carrera y calificar cursos.",
    version="1.0",
    contact={
        "name" : "Facundo Brun",
        "url" : "https://github.com/facubrun"
    },
    license_info={
        "name" : "Apache 2.0",
        "url" : "https://apache.org/licenses/LICENSE-2.0.html"
    },
    openapi_tags=tags_metadata,
    )

# Configuracion del APIRestFUL

# Endpoint GET /
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Endpoint GET /ingredientes
@app.get("/cursos",tags=["courses"])
async def read_courses():
    #await pedir datos
    return {"Objeto": "curso"}