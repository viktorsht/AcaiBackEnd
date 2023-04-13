import random

def generate_delivery_code():
    code = random.randint(1000, 9999)
    return code

#print(f"A senha do seu pedido é: {generate_delivery_code()}")
