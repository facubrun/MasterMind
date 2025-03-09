from random import randint


def main():
    numero_a_adivinar = randint(0,10)
    numero = int(input("Ingrese un numero del 0 al 10 para adivinar:\n"))
    if numero_a_adivinar == numero:
        print("Has acertado!")
    else:
        print("No es el numero correcto :/")

if __name__ == "__main__":
    main()