from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioComponente():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        componentes = self.session.query(models.Componente).all()
        return componentes