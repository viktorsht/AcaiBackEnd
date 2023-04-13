from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioPedido():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, pedido: schemas.Pedido):
        db_pedido = models.Pedido(
            codigo_entrega=pedido.codigo_entrega, #sera?
            id_estabelecimento=pedido.id_estabelecimento,
            id_produto=pedido.id_produto,
            id_cliente=pedido.id_cliente,
            id_endereco=pedido.id_endereco,
            id_pagamento=pedido.id_pagamento,
            observacao=pedido.observacao
        )
        self.session.add(db_pedido)
        self.session.commit()
        self.session.refresh(db_pedido)
        return db_pedido

    def listar(self):
        pedidos = self.session.query(models.Pedido).all()
        return pedidos