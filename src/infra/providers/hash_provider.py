from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bcrypt'])
        
def hash_password(password):
    return pwd_context.hash(password)

def hash_password_check(texto, hash):
    return pwd_context.verify(texto, hash)


