from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioRecipiente():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        recipiente = self.session.query(models.Recipiente).all()
        return recipiente