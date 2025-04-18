import os
import random
from pprint import pprint

from pokemon2.pokeLoad import get_all_pokemons


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def get_player_profile(pokemon_list):
    return {
        "player_name": input("Cual es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for p in range(3)],
        "combats": 0,
        "pokeballs": 0,
        "health_potion": 0,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def choose_pokemon(player_profile):
    clear_console()
    print("Elige un pokemón para el combate")
    for index in range(len(player_profile["pokemon_inventory"])):
        if player_profile["pokemon_inventory"][index]["current_health"] > 0:
            print("{} {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))

    while True:
        choose = input("¿Cual es tu eleccion?" )
        if choose.isdigit() and 0 <= int(choose) < len(player_profile["pokemon_inventory"]):
            clear_console()
            return player_profile["pokemon_inventory"][int(choose)]
        else:
            print("Eleccion invalida")


def get_pokemon_info(pokemon):
    return "{} | lvl {} | hp {}/{}".format(pokemon["name"],
                                           pokemon["level"],
                                           pokemon["current_health"],
                                           pokemon["base_health"])


def multiplier_weakness(attacker_type, defender_type):
    weaknesses = {
        "Fuego": ["Agua", "Tierra", "Roca"],
        "Agua": ["Planta", "Eléctrico"],
        "Planta": ["Fuego", "Hielo", "Veneno", "Volador", "Bicho"],
        "Eléctrico": ["Tierra"],
        "Normal": ["Lucha"],
        "Lucha": ["Volador", "Psíquico", "Hada"]
    }
    if defender_type in weaknesses.get(attacker_type,[]):
        return 1.28
    return 1


def choose_attack(pokemon):
    clear_console()
    print("Elige un ataque:")
    valid_attacks = [atk for atk in pokemon["attacks"] if atk["damage"] > 0]

    for i, atk in enumerate(valid_attacks):
        print(f"{i + 1}. {atk['name']} (Tipo: {atk['type']}, Daño: {atk['damage']})")

    while True:
        choice = input(">> ")
        if choice.isdigit() and 1 <= int(choice) <= len(valid_attacks):
            clear_console()
            return valid_attacks[int(choice) - 1]
        print("Opción inválida")


def player_attack(player_pokemon, enemy_pokemon):
    attack = choose_attack(player_pokemon)
    print(f"Turno del usuario: {player_pokemon['name']} usa {attack['name']} contra {enemy_pokemon['name']}")
    multiplier = multiplier_weakness(attack["type"], enemy_pokemon["type"][0])
    damage = int(attack["damage"] * multiplier)
    enemy_pokemon["current_health"] -= damage
    enemy_pokemon["current_health"] = max(0, enemy_pokemon["current_health"])
    print(f"{player_pokemon['name']} hizo {damage} de daño!\n\n")


def enemy_attack(enemy_pokemon, player_pokemon):
    attack = random.choice(enemy_pokemon["attacks"])
    print(f"Turno del enemigo: {enemy_pokemon['name']} usa {attack['name']} contra {player_pokemon['name']}")
    multiplier = multiplier_weakness(attack["type"], player_pokemon["type"][0])
    damage = int(attack["damage"] * multiplier)
    player_pokemon["current_health"] -= damage
    player_pokemon["current_health"] = max(0, player_pokemon["current_health"])
    print(f"{enemy_pokemon['name']} hizo {damage} de daño!\n\n")


def assign_xp(player_pokemon):
    points = random.randint(5, 10)
    player_pokemon["current_exp"] += points
    print(f"{player_pokemon['name']} ganó {points} de experiencia.")
    while player_pokemon["current_exp"] >= 20:
        player_pokemon["current_exp"] -= 20
        player_pokemon["level"] += 1
        player_pokemon["base_health"] += 10
        player_pokemon["current_health"] = player_pokemon["base_health"]
        print(f"¡{player_pokemon['name']} subió al nivel {player_pokemon['level']}!\n")


def capture_with_pokeball(player_profile, enemy_pokemon):
    if player_profile["pokeballs"] == 0:
        print("¡No tienes pokéballs!\n")
        return
    player_profile["pokeballs"] -= 1
    capture_chance = 100 - (enemy_pokemon["current_health"] * 100 // enemy_pokemon["base_health"])
    if random.randint(0, 100) < capture_chance:
        print(f"¡Capturaste a {enemy_pokemon['name']}!")
        player_profile["pokemon_inventory"].append(enemy_pokemon)
    else:
        print("El pokémon enemigo se escapó!\n")


def cure_pokemon(player_profile, pokemon):
    if player_profile["health_potion"] == 0:
        print("¡No tienes pociones!\n")
        return
    player_profile["health_potion"] -= 1
    health = 50
    pokemon["current_health"] = min(pokemon["current_health"] + health, pokemon["base_health"])
    print(f"{pokemon['name']} ha sido curado. Vida actual: {pokemon['current_health']}\n")


def item_lottery(player_profile):
    item = random.choice(["pokeballs", "health_potion"])
    player_profile[item] += 1
    print(f"¡Ganaste una {item}!\n")


def show_combat_status(player_profile, enemy_pokemon, player_pokemon):
    clear_console()
    print("\n--- Estado del Combate ---")
    for p in player_profile["pokemon_inventory"]:
        print(get_pokemon_info(p))
    print("Pokemon elegido:", get_pokemon_info(player_pokemon))
    print("Enemigo:", get_pokemon_info(enemy_pokemon))
    print(f"Pokéballs: {player_profile['pokeballs']} | Pociones: {player_profile['health_potion']}\n")


def fight(player_profile, enemy_pokemon):
    clear_console()
    print("---> NUEVO COMBATE <---\n")

    player_pokemon = choose_pokemon(player_profile)
    print("\n{} vs. {}\n".format(get_pokemon_info(player_pokemon),
                             get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and player_pokemon["current_health"] > 0 and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "V", "C", "E"]:
            action = input("Que deseas hacer? [A]tacar" 
                           "/ [P]okeball / Poción de [V]ida" 
                           "/ [C]ambiar / [E]stado del combate\n")

            if action == "A":
                player_attack(player_pokemon,enemy_pokemon)
                enemy_attack(enemy_pokemon, player_pokemon)

            elif action == "P":
                capture_with_pokeball(player_profile,enemy_pokemon)

            elif action == "V":
                cure_pokemon(player_profile,player_pokemon)

            elif action == "C":
                player_pokemon = choose_pokemon(player_profile)

            elif action == "E":
                show_combat_status(player_profile, enemy_pokemon, player_pokemon)

    if enemy_pokemon["current_health"] == 0:
        print("Has ganado!")
        assign_xp(player_pokemon)
        player_profile["combats"] += 1
    else: #perdio el usuario
        print(f"Perdiste en el combate {player_profile['combats']}.")

    print("---> FIN DEL COMBATE <---\n")
    input("Presiona ENTER para continuar.\n")


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    pprint(player_profile)
    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        if any_player_pokemon_lives(player_profile):
            item_lottery(player_profile)
        else:
            print("---> FIN DEL JUEGO <---")


if __name__ == "__main__":
    main()
