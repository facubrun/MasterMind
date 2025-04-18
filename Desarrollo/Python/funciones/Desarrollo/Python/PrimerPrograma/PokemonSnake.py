import os
import random
from random import randint
import readchar


# presentation of the game
print("Bienvenido al juego Pokemon-Snake, tendrás que recorrer con Snake el laberinto y enfrentar a entrenadores Pokémon\n"
      "(aparecen en el mapa con la D) cada uno de ellos tiene un Pokémon que podrá repetirse y tú debes vencerlos con Pikachu!\n"
      "Ganas el juego si vences a todos los entrenadores del mapa. Mucha suerte!\n")
input("Presiona Enter para continuar...\n")
os.system("cls")
#CONSTANTES

POS_X = 0
POS_Y = 1

NUM_OF_COACHES = 5
VIDA_INICIAL = 77
TAMANIO_BARRA = 10

#pokemons list
pokemons = ["Squirtle","Rattata","Eevee","Charizard","Bulbasur","Charmander"]
# attacks list
pokemon_attacks = {
    "Squirtle": [("Agua pegajosa", 10), ("Dientes mojados", 11)],
    "Rattata": [("Mordisco veloz", 8), ("Arañazo", 10)],
    "Eevee": [("Golpe rápido", 9), ("Placaje", 9)],
    "Charizard": [("Llamas", 12), ("Giro fuego", 11)],
    "Bulbasur": [("Drenadoras", 7), ("Latigo", 11)],
    "Charmander": [("Fuego salvaje", 11), ("Garra de fuego", 10)]
}
my_position = [0,1] # initial position
map_objects = []

obstacle_definition = """\
###########################
                       ####
     #############     ####
##    ##########       ####
###     #                 #
###    ####   ####    #####
####                     ##
########       #          #
#####                   ###
####        #####         #
########                ###
########      ####        #
#####      #########   ####
###########################\
"""

end_game = False
died = False
fin_victoria = False

# create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")] # crea lists of rows

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# generate random objects on the map
while len(map_objects) < NUM_OF_COACHES:
    new_position = [randint(0, MAP_WIDTH - 1), randint(0, MAP_HEIGHT - 1)]
    if new_position not in map_objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        map_objects.append(new_position)

# main loop
while not end_game:
    os.system("cls")

    # draw the map
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:
                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " D"
                    object_in_cell = map_object

            if coordinate_x == my_position[POS_X] and coordinate_y == my_position[POS_Y]:
                char_to_draw = " @"

                if object_in_cell: # Combate pokemon
                    os.system("cls")
                    input("\nPresiona Enter para iniciar el combate!\n")
                    os.system("cls")

                    vida_pikachu = VIDA_INICIAL
                    vida_oponente = VIDA_INICIAL
                    nombre_oponente = random.choice(pokemons)

                    while vida_oponente > 0 and vida_pikachu > 0:

                        # Turno de oponente
                        print("Es el turno de tu oponente!\n")
                        ataque_oponente = random.choice(pokemon_attacks[nombre_oponente])
                        print("{} ataca con {}".format(nombre_oponente, ataque_oponente[0]))
                        vida_pikachu -= ataque_oponente[1]

                        cantidad_vida_pikachu = int((vida_pikachu * TAMANIO_BARRA) / VIDA_INICIAL)
                        cantidad_vida_oponente = int((vida_oponente * TAMANIO_BARRA) / VIDA_INICIAL)

                        vida_pikachu = max(0, vida_pikachu)
                        vida_oponente = max(0, vida_oponente)

                        print("Pikachu  [{}{}] ({}/{})".format(
                                "#" * cantidad_vida_pikachu," " * (TAMANIO_BARRA - cantidad_vida_pikachu),
                                                                 vida_pikachu, VIDA_INICIAL) + "\n"
                                "{} [{}{}] ({}/{})".format(nombre_oponente,
                                    "#" * cantidad_vida_oponente, " " * (TAMANIO_BARRA - cantidad_vida_oponente),
                                    vida_oponente, VIDA_INICIAL) + "\n")
                        input("Enter para continuar...\n\n")
                        os.system("cls")

                        # Turno de Pikachu - Snake
                        print("Es tu turno!\n")
                        ataque_pikachu = None
                        while ataque_pikachu not in ["B", "R", "T", "N"]:
                            ataque_pikachu = input(
                                "Que ataque deseas realizar: [B]ola Amarilla, [R]ayos Gamma, [T]ruenos, [N]o atacar: ")

                        if ataque_pikachu == "B":
                            print("Pikachu ataca con Bola Amarilla")
                            vida_oponente -= 10
                        elif ataque_pikachu == "R":
                            print("Pikachu ataca con Rayos Gamma")
                            vida_oponente -= 12
                        elif ataque_pikachu == "T":
                            print("Pikachu ataca con Truenos")
                            vida_oponente -= 9
                        elif ataque_pikachu == "N":
                            print("Pikachu no ataca")

                        # Mostrar barra de vida después del ataque de Pikachu
                        cantidad_vida_pikachu = int((vida_pikachu * TAMANIO_BARRA) / VIDA_INICIAL)
                        cantidad_vida_oponente = int((vida_oponente * TAMANIO_BARRA) / VIDA_INICIAL)

                        vida_pikachu = max(0, vida_pikachu)
                        vida_oponente = max(0, vida_oponente)

                        print("Pikachu  [{}{}] ({}/{})".format(
                            "#" * cantidad_vida_pikachu, " " * (TAMANIO_BARRA - cantidad_vida_pikachu),
                            vida_pikachu, VIDA_INICIAL) + "\n"
                            "{} [{}{}] ({}/{})".format(nombre_oponente,
                                "#" * cantidad_vida_oponente, " " * (TAMANIO_BARRA - cantidad_vida_oponente),
                            vida_oponente, VIDA_INICIAL) + "\n")

                        input("Enter para continuar...\n\n")
                        os.system("cls")

                        # who wins?
                        if vida_pikachu == 0:
                            print("El entrenador oponente gana!")
                            input("\nPresiona Enter para continuar...\n")
                            os.system("cls")
                            my_position = [0, 1]
                        elif vida_oponente == 0:
                            print("Pikachu gana!")
                            input("\nPresiona Enter para continuar...\n")
                            os.system("cls")
                            map_objects.remove(object_in_cell)

                        os.system("cls")

                if len(map_objects) == 0:
                    end_game = True
                    fin_victoria = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    #ask the user where he wants to move
    direction = readchar.readchar()
    new_position = None
    if direction == "w" or direction == "W":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]
    elif direction == "s" or direction == "S":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]
    if direction == "a" or direction == "A":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "d" or direction == "D":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
    elif direction == "q" or direction == "Q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            my_position = new_position

    os.system("cls")
if fin_victoria:
    print("Ganaste!. Has vencido a todos los entrenadores!")
