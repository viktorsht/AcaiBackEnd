from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioProduto():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            volume_id=produto.volume_id,
            preco=produto.preco,
        )
        self.session.add(db_produto)
        self.session.commit()
        self.session.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.session.query(models.Produto).all()
        return produtos
    
    def listar_produto_id(self, produto_id: int):
        stmt = select(models.Produto).where(models.Produto.id == produto_id)
        user = self.db.execute(stmt)
        return user.scalar()
