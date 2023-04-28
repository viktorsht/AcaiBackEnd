from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric, DateTime
from datetime import datetime
from src.infra.sqlalchemy.config.database import Base

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(50))
    numero = Column(Integer)
    bairro = Column(String(50))
    complemento = Column(String)

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    telefone = Column(String(20))
    senha = Column(String(100))

class Volume(Base):
    __tablename__ = 'volume'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))

class Produto(Base):
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    descricao = Column(String)
    volume_id = Column(Integer, ForeignKey('volume.id' , name='volume_id'))
    preco = Column(Numeric(10,2))

class Pagamento(Base):
    __tablename__ = 'pagamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))

class Pedido(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey('produto.id' , name='produto_id')) 
    cliente_id = Column(Integer, ForeignKey('cliente.id' , name='cliente_id')) 
    endereco_id = Column(Integer, ForeignKey('endereco.id' , name='endereco_id')) 
    pagamento_id = Column(Integer, ForeignKey('pagamento.id' , name='id_pagamento')) 
    observacao = Column(String)
