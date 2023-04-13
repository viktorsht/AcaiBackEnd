from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.product.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=schemas.Produto)
def signup(produto: schemas.Produto, session: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(session).criar(produto)
    return produto_criado

@router.get('/produtos', response_model=List[schemas.Produto])
def listar_produtos(session: Session = Depends(get_db)):
    produtos = RepositorioProduto(session).listar()
    return produtos