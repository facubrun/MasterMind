import random
from io import BytesIO

from PIL import Image
from requests_html import HTMLSession
from speak_and_listen import speak, hear_me


def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            price = price.replace(",",".").replace(" con ", ".").replace("$", "").replace(" dolares", "")
            final_price = float(price)
            return final_price
        except ValueError:
            speak("No te he entendido, repite...")


def get_thot_session(session):
    categories = {
        "notebooks": "https://thotcomputacion.com.uy/categoria-producto/notebooks-y-accesorios/notebooks/",
        "tablets": "https://thotcomputacion.com.uy/categoria-producto/tablet/",
        "juegos": "https://thotcomputacion.com.uy/categoria-producto/juegos/",
        "tv": "https://thotcomputacion.com.uy/categoria-producto/tv/",
        "consolas": "https://thotcomputacion.com.uy/categoria-producto/consolas/"
    }
    speak("Elige la categoria para comenzar")
    category = hear_me()
    url = categories[category]
    return url

def get_random_product(url, session):
    image_src = None
    product_page = session.get(url)
    products = product_page.html.find(".main-content-wrap")
    product = random.choice(products)

    image = product.find(".img-effect", first=True)
    if image:
        image_tag = image.find("img", first=True)
        if image_tag:
            image_src = image_tag.attrs["data-src"]

    product_name = product.find(".woocommerce-loop-product__title", first=True).text
    product_price = product.find(".woocommerce-Price-amount", first=True).text

    return image_src, product_name, product_price

def show_image(session,image_src):
    img_downloaded = session.get(image_src)
    image = Image.open(BytesIO(img_downloaded.content))
    image.show()

def users_guess_and_return(user1_guess,user2_guess,product_price,user1_points,user2_points):
    if user1_points == 5:
        speak("El usuario 1 ha ganado el juego.")
    if user2_points == 5:
        speak("El usuario 2 ha ganado el juego.")
    if abs(user1_guess - product_price) < abs(user2_guess - product_price):
        speak("El usuario 1 suma un punto.")
        user1_points += 1
    else:
        speak("El usuario 2 suma un punto.")
        user2_points += 1

    speak("El precio era {}".format(product_price))


def main():
    user1_points = 0
    user2_points = 0

    #speak("Bienvenido al precio justo, vamos a intentar adivinar los precios de algunos productos")
    session = HTMLSession()

    while user1_points < 5 and user2_points < 5:
        url = get_thot_session(session)
        image_src, product_name, product_price = get_random_product(url, session)

        show_image(session, image_src)
        print(product_name)
        speak("El nombre del producto es {}, cuanto crees que vale?".format(product_name))

        speak("Turno del usuario 1:")
        user1_guess = hear_price_and_get_number()
        speak("Turno del usuario 2:")
        user2_guess = hear_price_and_get_number()

        price_number = product_price.replace("US$", "")
        users_guess_and_return(float(user1_guess),float(user2_guess),float(price_number),user1_points,user2_points)


if __name__ == "__main__":
    main()