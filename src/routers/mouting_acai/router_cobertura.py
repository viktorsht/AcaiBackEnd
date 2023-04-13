from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.mounting_acai.repositorio_cobertura import RepositorioCobertura
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/coberturas', response_model=List[schemas.Cobertura])
def listar_coberturas(session: Session = Depends(get_db)):
    coberturas = RepositorioCobertura(session).listar()
    return coberturas