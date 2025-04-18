import pickle
from requests_html import HTMLSession


pokemon_base = {
    "name": "",
    "attacks": None,
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0
}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

def get_pokemon(index):
    url = "{}{}".format(URL_BASE, index)
    session = HTMLSession()

    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)

    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text.splitlines()[0]
    new_pokemon["type"] = []
    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])

    new_pokemon["attacks"] = []
    for attack_item in pokemon_page.html.find(".pkmain")[-1].find("tr .check3"):  # indice del ultimo
        attack = {
            "name": attack_item.find("td", first=True).find("a",first=True).text,
            "type": attack_item.find("td")[1].find("img", first=True).attrs["alt"],
            "min_level": attack_item.find("th")[1].text,
            "damage": int(attack_item.find("td")[3].text.replace("--","0"))
        }
        if attack["damage"] > 0:
            new_pokemon["attacks"].append(attack)
    return new_pokemon

def get_all_pokemons():
    try:
        with open("pokefile.pkl", "rb") as pokefile:
            print("Cargando el archivo...")
            all_pokemons = pickle.load(pokefile)
    except FileNotFoundError:
        print("Archivo no encontrado, descargando de internet...")
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index + 1))
            print("*",end="")
        print("Todos los pokemons han sido descargados.")

        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)

    return all_pokemons
