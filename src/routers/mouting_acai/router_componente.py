from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.mounting_acai.repositorio_componente import RepositorioComponente
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/componentes', response_model=List[schemas.Acompanhamento])
def listar_componentes(session: Session = Depends(get_db)):
    componentes = RepositorioComponente(session).listar()
    return componentes