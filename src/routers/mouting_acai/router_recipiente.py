from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.mounting_acai.repositorio_recipiente import RepositorioRecipiente
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/recipientes', response_model=List[schemas.Recipiente])
def listar_recipientes(session: Session = Depends(get_db)):
    recipientes = RepositorioRecipiente(session).listar()
    return recipientes