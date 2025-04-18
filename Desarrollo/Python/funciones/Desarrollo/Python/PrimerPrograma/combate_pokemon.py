from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
vida_pikachu = VIDA_INICIAL_PIKACHU

VIDA_INICIAL_SQUIRTLE = 90
vida_squirtle = VIDA_INICIAL_SQUIRTLE

TAMANIO_BARRA = 10

while vida_squirtle > 0 and vida_pikachu >0:

    #Turno de pikachu CPU
    print("Turno de pikachu")
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        vida_squirtle -= 11

    cantidad_vida_pikachu = int((vida_pikachu * TAMANIO_BARRA) / VIDA_INICIAL_PIKACHU)
    cantidad_vida_squirtle = int((vida_squirtle * TAMANIO_BARRA) / VIDA_INICIAL_SQUIRTLE)

    if vida_squirtle < 0:
        vida_squirtle = 0
    print(
        "Pikachu  [{}{}] ({}/{})".format("#" * cantidad_vida_pikachu, " " * (TAMANIO_BARRA - cantidad_vida_pikachu),
                                         vida_pikachu, VIDA_INICIAL_PIKACHU) + "\n"
        "Squirtle [{}{}] ({}/{})".format("#" * cantidad_vida_squirtle, " " * (TAMANIO_BARRA - cantidad_vida_squirtle),
                                         vida_squirtle,VIDA_INICIAL_SQUIRTLE) + "\n")
    input("Enter para continuar...\n\n")
    os.system("cls")

    #Turno de Squirtle
    print("Turno de squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["P", "A", "B", "N"]:
        ataque_squirtle = input("Que ataque deseas realizar: [P]lacaje, Pistola [A]gua, [B]urbuja, [N]o atacar: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("Squirtle no ataca")

    cantidad_vida_pikachu = int((vida_pikachu * TAMANIO_BARRA) / VIDA_INICIAL_PIKACHU)
    cantidad_vida_squirtle = int((vida_squirtle * TAMANIO_BARRA) / VIDA_INICIAL_SQUIRTLE)

    if vida_pikachu < 0:
        vida_pikachu = 0
    print("Pikachu  [{}{}] ({}/{})".format("#" * cantidad_vida_pikachu, " " * (TAMANIO_BARRA - cantidad_vida_pikachu),
                                           vida_pikachu, VIDA_INICIAL_PIKACHU) + "\n"
        "Squirtle [{}{}] ({}/{})".format("#" * cantidad_vida_squirtle, " " * (TAMANIO_BARRA - cantidad_vida_squirtle),
                                         vida_squirtle, VIDA_INICIAL_SQUIRTLE) + "\n")

    input("Enter para continuar...\n\n")
    os.system("cls")

if vida_pikachu == 0:
    print("Squirtle gana!")
elif vida_squirtle == 0:
    print("Pikachu gana!")