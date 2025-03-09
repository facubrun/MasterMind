from selenium import webdriver
from time import sleep
from requests_html import HTMLSession
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

def stock_in_pccomponentes(url,session):
    while True:
        product_page = session.get(url)
        buy_zone = product_page.html.find("#btnsWishAddBuy") # Busca un id (#) que coincida con 'btnsWishAddBuy'
        if len(buy_zone) > 0:
            print("Hay stock!")
            break
        else:
            print("Sigue sin haber stock :(")

        sleep(30)  # Lo hace cada 30seg


def stock_in_coolmod(url,session):
    while True:
        product_page = session.get(url)
        found = product_page.html.find(".btn-primary.add-to-cart")
        if len(found) > 0:
            driver = webdriver.Firefox()
            driver.get(url)
            close_pop_ups(driver)
            confirm_buy(driver)
            complete_form(driver)
        else:
            print("No hay stock :(")


def close_pop_ups(driver):
    sleep(5)
    try:
        driver.find_element(By.ID,"CybotCookiebotDialogBodyButtonDecline").click()
        sleep(5)
        driver.find_element(By.CSS_SELECTOR,".cn_content_close-adf93cbc-6fdd-46b7-9fe6-32ed75f57ade a").click()
        sleep(3)
        driver.find_element(By.CSS_SELECTOR, "svg.w-8.h-8.close-icon path").click()
        sleep(3)
    except NoSuchElementException:
        print("No es posible cerrar pop-ups")


def confirm_buy(driver):
    sleep(3)
    try:
        driver.find_element(By.CSS_SELECTOR, "div.flex.flex-col.gap-2 button.btn.btn-primary.add-to-cart").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-primary.flex-1").click()
    except NoSuchElementException:
        print("No se puede comprar")

def complete_form(driver):
    is_form_loaded = None
    form = None
    while not is_form_loaded:
        try:
            form = driver.find_element(By.ID, "form-login")
            is_form_loaded = True
        except NoSuchElementException:
            print("El formulario aun no cargó")
    email = form.find_element(By.ID, "user-email")
    password = form.find_element(By.ID, "user-password")

    email.send_keys("bot@bot.com")
    password.send_keys("bot1234")

    driver.find_element(By.ID, "btn-login").click()


def main():
    url_pc_componentes = "https://www.pccomponentes.com/portatil-asus-vivobook-15-m1502ya-nj506w-amd-ryzen-7-7730u-16gb-512gb-ssd-156"
    url_coolmod = "https://www.coolmod.com/asus-proart-geforce-rtx-4060-ti-oc-16gb-gddr6x-dlss3/"

    session = HTMLSession()

    #stock_in_pccomponentes(url_pc_componentes, session)
    stock_in_coolmod(url_coolmod, session)

if __name__ == "__main__":
    main()