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