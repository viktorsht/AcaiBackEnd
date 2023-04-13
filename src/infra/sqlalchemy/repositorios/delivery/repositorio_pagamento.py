from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models

class RepositorioPagamento():

    def __init__(self, session: Session):
        self.session = session

    def listar(self):
        pagamentos = self.session.query(models.Pagamento).all()
        return pagamentos