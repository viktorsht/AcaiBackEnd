from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioCobertura():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        coberturas = self.session.query(models.Cobertura).all()
        return coberturas