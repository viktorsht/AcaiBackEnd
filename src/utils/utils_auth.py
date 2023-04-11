from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_clientes import RepositorioCliente
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_schema), session: Session() = Depends(get_db)):

    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    
    try:
        telefone = token_provider.check_access_token(token)
    except JWTError:
        raise exception
    
    if not telefone:
        raise exception

    usuario = RepositorioCliente(session).verificar_telefone(telefone)

    if not usuario:
        raise exception

    return usuario

