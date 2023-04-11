from jose import jwt
from datetime import datetime, timedelta

SECRETY_KEY = '$2b$12$I4cKM6aQMNA1ER1Eb.yqteIFnons1CyNZWRwgea0AgqAK993TVl7e'
ALGORITHM = 'HS256'
EXPIRE_IN_MIN = 3000

def create_access_token(data: dict):
    return pwd_context.hash(password)

def check_access_token(token):
    return pwd_context.verify(texto, hash)