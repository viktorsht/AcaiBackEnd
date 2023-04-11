from jose import jwt
from datetime import datetime, timedelta

SECRETY_KEY = '$2b$12$I4cKM6aQMNA1ER1Eb.yqteIFnons1CyNZWRwgea0AgqAK993TVl7e'
ALGORITHM = 'HS256'
EXPIRE_IN_MIN = 3000

def create_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRE_IN_MIN)
    dados.update({'exp' : expiracao})
    token_jwt = jwt.encode(dados, SECRETY_KEY, algorithm=ALGORITHM)
    return token_jwt

def check_access_token(token):
    carga = jwt.decode(token, SECRETY_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')