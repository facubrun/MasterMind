import random

from requests_html import HTMLSession
from speak_and_listen import speak, hear_me


def main():
    speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")
    session = HTMLSession()
    main_page = session.get("https://www.pccomponentes.com")
    categories = main_page.html.find(".sc-dGcaAO")
    print(categories)
    category = random.choice(categories)


if __name__ == "__main__":
    main()