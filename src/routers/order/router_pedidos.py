from fastapi import APIRouter, Depends, status
import datetime
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.order.repositorio_pedidos import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from src.utils.generator_delivery_code import generate_delivery_code
from src.utils.time import generate_time

router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas.PedidoSimples)
def signup(pedido: schemas.Pedido, session: Session = Depends(get_db)):
    pedido.codigo_entrega = generate_delivery_code()
    #pedido.horario = generate_time()
    pedido_criado = RepositorioPedido(session).criar(pedido)
    return pedido_criado

@router.get('/pedidos', response_model=List[schemas.Pedido])
def listar_pedidos(session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar()
    return pedidos