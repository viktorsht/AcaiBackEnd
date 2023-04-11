from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_estabelecimento import RepositorioEstabelecimento
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/localization', response_model=List[schemas.EstabelecimentoInitial])
def minha_localizacao(session: Session = Depends(get_db)):
    estabelecimento = RepositorioEstabelecimento(session).listar()
    return estabelecimento

@router.get('/estabelecimentos', response_model=List[schemas.Estabelecimento])
def listar_cidades_com_estabelecimento(session: Session = Depends(get_db)):
    estabelecimento = RepositorioEstabelecimento(session).listar()
    return estabelecimento