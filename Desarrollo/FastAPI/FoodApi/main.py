from fastapi import FastAPI

# Objeto app de tipo FastAPI
app = FastAPI()

# Configuracion del APIRestFUL

# Entrada GET http://localhost/
@app.get("/")
def read_root():
    return {"Hello": "World"}