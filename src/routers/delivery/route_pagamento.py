from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.delivery.repositorio_pagamento import RepositorioPagamento
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter()

@router.get('/pagamentos', response_model=List[schemas.Pagamento])
def listar_pagamentos(session: Session = Depends(get_db)):
    pagamentos = RepositorioPagamento(session).listar()
    return pagamentos