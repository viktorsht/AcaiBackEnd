from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.repositorio_clientes import RepositorioCliente
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import hash_provider, token_provider
from src.utils.utils_auth import obter_usuario_logado

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.ClienteCadastrado)
def signup(cliente: schemas.Cliente, db: Session = Depends(get_db)):
    cliente_encontrado = RepositorioCliente(db).verificar_telefone(cliente.telefone)
    if cliente_encontrado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Este telefone já está em uso!")
    cliente.senha = hash_provider.hash_password(cliente.senha)
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@router.post('/token', status_code=status.HTTP_200_OK, response_model=schemas.LoginSucess)
def login(login_data: schemas.Login, db: Session = Depends(get_db)):
    senha = login_data.senha
    telefone = login_data.telefone
    usuario = RepositorioCliente(db).verificar_telefone(telefone)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Telefone ou senha incorretos!")
    
    senha_valida = hash_provider.hash_password_check(senha, usuario.senha)
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Telefone ou senha incorretos!")
    
    token  = token_provider.create_access_token({'sub' : usuario.telefone})

    return schemas.LoginSucess(cliente=usuario,token=token)

@router.get('/me', status_code=status.HTTP_200_OK, response_model=schemas.ClienteCadastrado)
def meu_perfil(cliente: schemas.Cliente = Depends(obter_usuario_logado)):
    return cliente
    







@router.get('/clientes', response_model=List[schemas.Cliente])
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@router.get('/clientes/{id_user}', status_code=status.HTTP_200_OK, response_model=schemas.ClienteCadastrado)
def listar_cliente_id(id_user: int, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).listar_usuario(id_user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente não encontrado!")
    return user

@router.put('/clientes/{id_user}')
def atualizar_cliente(id_user: int, cliente: schemas.Cliente, db: Session = Depends(get_db)):
    user = RepositorioCliente(db).atualizar(id_user, cliente)
    return user

@router.delete('/clientes/{id_user}', status_code=status.HTTP_200_OK)
def remover_cliente(id_user: int, db: Session = Depends(get_db)):
    RepositorioCliente(db).remover(id_user)
    return {"data" : "Removido com sucesso!"}