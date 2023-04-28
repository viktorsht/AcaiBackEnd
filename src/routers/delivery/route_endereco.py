from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.delivery.repositorio_endereco import RepositorioEndereco
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/enderecos', status_code=status.HTTP_201_CREATED, response_model=schemas.Endereco)
def signup(endereco: schemas.Endereco, session: Session = Depends(get_db)):
    endereco_criado = RepositorioEndereco(session).criar(endereco)
    return endereco_criado

@router.get('/enderecos', response_model=List[schemas.Endereco])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioEndereco(session).listar()
    return produtos