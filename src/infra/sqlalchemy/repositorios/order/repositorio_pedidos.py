from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
            produto_id=pedido.id_produto,
            cliente_id=pedido.id_cliente,
            endereco_id=pedido.id_endereco,
            pagamento_id=pedido.id_pagamento,
            observacao=pedido.observacao
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        pedidos = self.session.query(models.Pedido).all()
        return pedidos
    
    def listar_pedidos(self, user_id: int):
        stmt = select(models.Pedido).where(models.Pedido.id_cliente == user_id)
        result = self.session.execute(stmt).scalars().all()
        #user = self.session.execute(stmt)
        #return user.scalar()
        return result