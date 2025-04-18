def potencia(numero):
    numero *= numero
    return numero


def main():
    numero = int(input("Ingresa un numero para obtener su potencia:"))
    print("La potencia del numero ingresado es: {}".format(potencia(numero)))


if __name__ == "__main__":
    main()
