from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioEndereco():

    def __init__(self, session: Session):
        self.session = session
    
    def criar(self, endereco: schemas.Endereco):
        db_endereco = models.Endereco(
            rua=endereco.rua,
            numero=endereco.numero,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
        )
        self.session.add(db_endereco)
        self.session.commit()
        self.session.refresh(db_endereco)
        return db_endereco
""" 
    def listar(self):
        enderecos = self.session.query(models.Endereco).all()
        return enderecos """
    