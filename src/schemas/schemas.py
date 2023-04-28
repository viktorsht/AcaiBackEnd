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

class Endereco(BaseModel):
    id: Optional[int] = None
    rua: str
    numero: int
    bairro: str
    complemento: str
    class Config:
        orm_mode = True

class Volume(BaseModel):
    id: Optional[int] = None
    nome: str
    class Config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str
    volume_id: int
    preco: str # talves dê erro por no banco ser float!
    class Config:
        orm_mode = True

class Pagamento(BaseModel):
    id: Optional[int] = None
    nome: str
    class Config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[int] = None
    id_produto: int
    id_cliente: Optional[int] = None
    id_endereco: int
    id_pagamento: int
    observacao: Optional[str] = None
    class Config:
        orm_mode = True

class PedidoSimples(BaseModel):
    id: Optional[int] = None
    id_produto: int
    class Config:
        orm_mode = True