from sqlalchemy import Column, Integer, String, ForeignKey, Text

from src.infra.sqlalchemy.config.database import Base

class InfoEmpresa(Base):
    __tablename__ = 'info_empresa'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    email = Column(String(50))
    descricao = Column(Text)
    instagram = Column(String(30))

class Adicional(Base):
    __tablename__ = 'adicional'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    preco = Column(Integer)

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    telefone = Column(String(20))
    senha = Column(String(100))