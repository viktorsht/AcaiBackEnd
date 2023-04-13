from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            id_recipiente=produto.id_recipiente,
            id_adicional=produto.id_adicional,
            id_componente=produto.id_componente,
            id_cobertura=produto.id_cobertura,
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos