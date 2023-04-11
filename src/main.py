from fastapi import FastAPI, APIRouter, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_clientes import RepositorioCliente
from src.infra.sqlalchemy.config.database import get_db


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

@app.get('/')
def init_api():
    return {'data' : 'API ok!'}

#caso queira retornar o id dos usuário é só retirar o -> response_model=schemas.Cliente

@app.post('/clientes', status_code=status.HTTP_201_CREATED, response_model=schemas.Cliente)
def cadastrar_clientes(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@app.get('/clientes', response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@app.get('/clientes/{id_user}', response_model=schemas.Cliente)
def obter_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).listar_usuario(id_user)
    return user

@app.put('/clientes/{user_id}')
def atualizar_cliente(user_id: int, cliente: schemas.Cliente, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).atualizar(user_id, cliente)
    return user

@app.delete('/clientes/{id_user}', response_model=schemas.Cliente)
def remover_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).remover(id_user)
    return {'data' : 'Removido com Sucesso!'}