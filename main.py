import random

def generator_password(valor: int):
    """
    Esta funcion crea una contrasena segura de 8 a 32 digitos
    """
    password = ''

    characters = list(range(33, 126))

    try:
        cantidad = valor
        if cantidad > 32:
            return False
        elif cantidad < 8:
            return False
        elif cantidad > 8:
            cantidad = cantidad
        elif cantidad < 32:
            cantidad = cantidad
    except:
        return 'Valor incorrecto'

    for i in range(cantidad):
        password += chr(random.choice(characters))

    return password





# def generator_password():
#     password = ''
#
#     characters = list(range(33, 126))
#     try:
#         cantidad = int(input('coloca un numero '))
#         if cantidad > 32:
#             return False
#         elif cantidad < 8:
#             return False
#         elif cantidad > 8:
#             cantidad = cantidad
#         elif cantidad < 32:
#             cantidad = cantidad
#     except:
#         return 'Valor incorrecto'
#
#     for i in range(cantidad):
#         password += chr(random.choice(characters))
#
#     return password
# print(generator_password())
