from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import router_usuarios, router_estabelecimento, router_recipiente, router_componente, router_adicional

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

app.include_router(router_usuarios.router, prefix='/api/auth')
app.include_router(router_estabelecimento.router, prefix='/api')
app.include_router(router_recipiente.router, prefix='/api')
app.include_router(router_componente.router, prefix='/api')
app.include_router(router_adicional.router, prefix='/api')

@app.get('/')
def init_api():
    return {'data' : 'API ok!'}