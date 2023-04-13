from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.mounting_acai.repositorrio_adicional import RepositorioAdicional
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/adicionais', response_model=List[schemas.Adicional])
def listar_adicionais(session: Session = Depends(get_db)):
    adicionais = RepositorioAdicional(session).listar()
    return adicionais