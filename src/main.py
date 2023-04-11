from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_usuarios
app = FastAPI()

origins = [
    'http://127.0.0.1:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_usuarios.router)

@app.get('/')
def init_api():
    return {'data' : 'API ok!'}

#caso queira retornar o id dos usuário é só retirar o -> response_model=schemas.Cliente