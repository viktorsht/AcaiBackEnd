from sqlalchemy import Column, Integer, String, ForeignKey, Text, Numeric
from src.infra.sqlalchemy.config.database import Base

class InfoEmpresa(Base):
    __tablename__ = 'info_empresa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    email = Column(String(50))
    descricao = Column(Text)
    instagram = Column(String(30))

class Estabelecimento(Base):
    __tablename__ = 'estabelecimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(50))
    numero = Column(Integer)
    bairro = Column(String(50))
    cidade = Column(String(50))
    telefone = Column(String(20))
    status_funcionamento = Column(Integer)

class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True, autoincrement=True)
    rua = Column(String(50))
    numero = Column(Integer)
    bairro = Column(String(50))
    cidade = Column(String(50))

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    telefone = Column(String(20))
    senha = Column(String(100))

class Recipiente(Base):
    __tablename__ = 'recipiente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    preco = Column(Numeric(10,2))
    volume = Column(Integer)

class Componente(Base):
    __tablename__ = 'componente'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20))


class Cobertura(Base):
    __tablename__ = 'cobertura'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20))


class Adicional(Base):
    __tablename__ = 'adicional'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(20))
    preco = Column(Numeric(10,2))

class Produto(Base):
    __tablename__ = 'produto'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_recipiente = Column(Integer,ForeignKey('recipiente.id' , name='id_recipiente'))
    id_adicional = Column(Integer, ForeignKey('adicional.id' , name='id_adicional'))
    id_componente = Column(Integer, ForeignKey('componente.id' , name='id_componente'))
    id_cobertura = Column(Integer, ForeignKey('cobertura.id' , name='id_cobertura'))

class Pagamento(Base):
    __tablename__ = 'pagamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(8))