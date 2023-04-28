from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.delivery import route_endereco, route_pagamento
from src.routers.product import router_produto
from src.routers.volume import router_volume
from src.routers.user import router_usuarios
from src.routers.order import router_pedidos

app = FastAPI()

origins = [
    'http://127.0.0.1:8000',
    'https://acaiteria-backend.vercel.app/'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_usuarios.router, prefix='/api/auth')
app.include_router(router_volume.router, prefix='/api')
app.include_router(router_produto.router, prefix='/api')
app.include_router(route_pagamento.router, prefix='/api')
app.include_router(route_endereco.router, prefix='/api')
app.include_router(router_pedidos.router, prefix='/api')

@app.get('/')
def init_api():
    return {'data' : 'API ok!'}