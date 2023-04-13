from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    class Config:
        orm_mode = True

class ClienteCadastrado(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    class Config:
        orm_mode = True

class Login(BaseModel):
    telefone: str
    senha: str

class LoginSucess(BaseModel):
    cliente: ClienteCadastrado
    token: str

class Estabelecimento(BaseModel):
    id: Optional[int] = None
    rua: str
    numero: int
    bairro: str
    cidade: str
    telefone: str
    status_funcionamento: int
    class Config:
        orm_mode = True
    
class EstabelecimentoInitial(BaseModel):
    id: Optional[int] = None
    cidade: str
    status_funcionamento: int
    class Config:
        orm_mode = True

class Endereco(BaseModel):
    id: Optional[int] = None
    rua: str
    numero: int
    bairro: str
    cidade: str
    class Config:
        orm_mode = True

class Recipiente(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    volume: str
    class Config:
        orm_mode = True

class Acompanhamento(BaseModel):
    id: Optional[int] = None
    nome: str
    class Config:
        orm_mode = True

class Cobertura(BaseModel):
    id: Optional[int] = None
    nome: str
    class Config:
        orm_mode = True

class Adicional(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    id_recipiente: int 
    id_adicional: int
    id_componente: int
    id_cobertura: int
    class Config:
        orm_mode = True

class Pagamento(BaseModel):
    id: Optional[int] = None
    tipo: str
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int] = None
    codigo_entrega: Optional[int] = None
    horario: Optional[datetime] = None
    id_estabelecimento: int 
    id_produto: int
    id_cliente: int
    id_endereco: int
    id_pagamento: int
    observacao: Optional[str] = None
    class Config:
        orm_mode = True

class PedidoSimples(BaseModel):
    id: Optional[int] = None
    codigo_entrega: Optional[int] = None
    class Config:
        orm_mode = True