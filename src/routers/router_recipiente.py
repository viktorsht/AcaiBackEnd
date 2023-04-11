from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_recipiente import RepositorioRecipiente
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/recipentes', response_model=List[schemas.Recipiente])
def minha_localizacao(session: Session = Depends(get_db)):
    estabelecimento = RepositorioRecipiente(session).listar()
    return estabelecimento