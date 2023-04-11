from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_clientes import RepositorioCliente
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/clientes', status_code=status.HTTP_201_CREATED, response_model=schemas.Cliente)
def cadastrar_clientes(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@router.get('/clientes', response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@router.get('/clientes/{id_user}', response_model=schemas.Cliente)
def obter_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).listar_usuario(id_user)
    return user

@router.put('/clientes/{user_id}')
def atualizar_cliente(user_id: int, cliente: schemas.Cliente, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).atualizar(user_id, cliente)
    return user

@router.delete('/clientes/{id_user}', response_model=schemas.Cliente)
def remover_cliente(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).remover(id_user)
    return {'data' : 'Removido com Sucesso!'}