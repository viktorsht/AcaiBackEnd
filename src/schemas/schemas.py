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

