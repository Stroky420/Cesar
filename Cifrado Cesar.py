# ingrese el mensaje y la clave
mensaje_original = input("Ingrese el mensaje a cifrar: ")
clave = int(input("Ingrese la clave para el cifrado César: "))

mensaje_cifrado = ""


# Alfabeto en mayúsculas y minúsculas
alfabeto_mayusculas = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
alfabeto_minusculas = list('abcdefghijklmnopqrstuvwxyz')

# Cifrado del mensaje
for caracter in mensaje_original:
    if 'A' <= caracter <= 'Z':
        indice_original = alfabeto_mayusculas.index(caracter)
        indice_cifrado = (indice_original + clave) % 26
        caracter_cifrado = alfabeto_mayusculas[indice_cifrado]
    elif 'a' <= caracter <= 'z':
        indice_original = alfabeto_minusculas.index(caracter)
        indice_cifrado = (indice_original + clave) % 26
        caracter_cifrado = alfabeto_minusculas[indice_cifrado]
    else:
        caracter_cifrado = caracter
    mensaje_cifrado += caracter_cifrado

print("Mensaje encriptado:", mensaje_cifrado)
mensaje_descifrado = ""
# Decifrado del mensaje
for caracter in mensaje_cifrado:
    if 'A' <= caracter <= 'Z':
        indice_cifrado = alfabeto_mayusculas.index(caracter)
        indice_descifrado = (indice_cifrado - clave) % 26
        caracter_descifrado = alfabeto_mayusculas[indice_descifrado]
    elif 'a' <= caracter <= 'z':
        indice_cifrado = alfabeto_minusculas.index(caracter)
        indice_descifrado = (indice_cifrado - clave) % 26
        caracter_descifrado = alfabeto_minusculas[indice_descifrado]
    else:
        caracter_descifrado = caracter
    mensaje_descifrado += caracter_descifrado

print("Mensaje descifrado:", mensaje_descifrado)