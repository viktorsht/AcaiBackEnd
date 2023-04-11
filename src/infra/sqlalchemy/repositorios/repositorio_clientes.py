from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioCliente():

    def __init__(self, db: Session):
        self.db = db

    def criar(self, cliente: schemas.Cliente):
        db_cliente = models.Cliente(
            nome=cliente.nome,
            telefone=cliente.telefone,
            senha=cliente.senha
        )
        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente


    def listar(self):
        clientes = self.db.query(models.Cliente).all()
        return clientes

    def obter(self, user_id: int):
        stmt = select(models.Cliente).where(models.Cliente.id == user_id)
        user = self.db.execute(stmt)
        return user.scalar()

    def remover(self, user_id: int):
        stmt = delete(models.Cliente).where(models.Cliente.id == user_id)
        self.db.execute(stmt)
        self.db.commit()