print("Lista de compras")

lista = []
eleccion = None

while True:
    eleccion = input("Que desea comprar? ([Q] para salir) \n")
    if eleccion == "Q":
        break
    elif eleccion not in lista:
        if input("Seguro que quieres añadir {} a la lista? [S/N]\n".format(eleccion)) == "S":
            lista.append(eleccion)
    else:
        print("{} ya está en la lista".format(eleccion))

print("Tu lista de compras es: {}".format(lista))