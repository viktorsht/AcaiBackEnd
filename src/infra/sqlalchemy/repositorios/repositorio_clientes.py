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

    def obter(self):
        pass

    def remover(self):
        pass