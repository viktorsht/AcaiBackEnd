from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioAdicional():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        adicional = self.session.query(models.Adicional).all()
        return adicional