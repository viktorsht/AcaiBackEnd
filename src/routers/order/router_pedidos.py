from fastapi import APIRouter, Depends, status, HTTPException
import datetime
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.order.repositorio_pedidos import RepositorioPedido
from src.infra.sqlalchemy.config.database import get_db
from src.utils.utils_auth import obter_usuario_logado

router = APIRouter()

@router.post('/pedidos', status_code=status.HTTP_201_CREATED, response_model=schemas.PedidoSimples)
def signup(pedido: schemas.Pedido, cliente: schemas.Cliente = Depends(obter_usuario_logado), session: Session = Depends(get_db)):
    pedido.id_cliente = cliente.id
    pedido_criado = RepositorioPedido(session).criar(pedido)
    return pedido_criado

@router.get('/pedidos', response_model=List[schemas.Pedido])
def listar_pedidos(session: Session = Depends(get_db)):
    pedidos = RepositorioPedido(session).listar()
    return pedidos

@router.get('/meuspedidos', status_code=status.HTTP_200_OK, response_model=List[schemas.Pedido])
def listar_cliente_id(cliente: schemas.Cliente = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    user = RepositorioPedido(db).listar_pedidos(cliente.id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pedidos não encontrado!")
    return user
