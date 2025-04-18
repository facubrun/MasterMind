texto_usuario = input("Escriba el texto que quieras:\n")

espacios = 0
puntos = 0
comas = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("El texto tiene {} espacios, {} puntos y {} comas.".format(espacios,puntos,comas))

