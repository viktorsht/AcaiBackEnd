from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.volume.repositorio_volume import RepositorioVolume
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/volumes', response_model=List[schemas.Volume])
def listar_recipientes(session: Session = Depends(get_db)):
    recipientes = RepositorioVolume(session).listar()
    return recipientes