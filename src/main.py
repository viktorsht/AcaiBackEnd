from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_clientes import RepositorioCliente
from src.infra.sqlalchemy.config.database import get_db


app = FastAPI()

@app.get('/')
def init_api():
    return {'data' : 'API ok!'}

@app.post('/clientes')
def cadastrar_clientes(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@app.get('/clientes')
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@app.get('/clientes/{id_user}')
def obter_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).obter(id_user)
    return user

@app.delete('/clientes/{id_user}')
def obter_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).remover(id_user)
    return {'data' : 'Removido com Sucesso!'}