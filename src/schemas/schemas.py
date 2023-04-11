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
    rua: str
    numero: int
    bairro: str
    cidade: str
    status_funcionamento: int
    class Config:
        orm_mode = True
    
class EstabelecimentoInitial(BaseModel):
    cidade: str
    status_funcionamento: int
    class Config:
        orm_mode = True

class Recipiente(BaseModel):
    nome: str
    preco: float
    volume: str
    class Config:
        orm_mode = True