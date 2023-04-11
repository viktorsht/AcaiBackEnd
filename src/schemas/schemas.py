from pydantic import BaseModel
from typing import List, Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    telefone: str
    senha: str
    class Config:
        orm_mode = True

