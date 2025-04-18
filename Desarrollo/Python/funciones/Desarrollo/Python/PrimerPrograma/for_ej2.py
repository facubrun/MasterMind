import string

texto_usuario = input("Introduzca un texto:\n")
lista_mayusculas = string.ascii_uppercase
mayusculas = 0

for letra in texto_usuario:
    if letra in lista_mayusculas:
        mayusculas += 1

print("Mayusculas: {}".format(mayusculas))