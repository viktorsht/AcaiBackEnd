from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioEstabelecimento():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        estabelecimentos = self.session.query(models.Estabelecimento).all()
        return estabelecimentos