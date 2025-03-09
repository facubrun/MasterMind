#EJ1
import os


def string_mas_largo(*args):
    mas_largo = 0
    tamanio_largo = 0
    for string in args:
        if len(string) > tamanio_largo:
            mas_largo = string
            tamanio_largo = len(string)

    return mas_largo, tamanio_largo

#EJ2
def suma(lista):
    suma = 0
    for elem in lista:
        suma += elem
    return suma

#EJ3
def es_impar(k):
    if k % 2 != 0:
        return True
    return False # Obs: si entra por la condicion del if solo se ejecuta ese return True y termina.

#EJ4
def decision():
    respuesta = input("Estas seguro? [S/N]: ")
    if respuesta == "S":
        return True
    return False

#EJ5
def a_mayus(string):
    resultado = ""
    for char in string:
        if "a" <= char <= "z":
            resultado += chr(ord(char) - 32)
        else:
            resultado += char
    return resultado

#EJ6
def adivinar(numero_adivinar):
    if numero_adivinar < 0 or numero_adivinar > 100:
      print("Por favor, ingrese un numero válido.")
    else:
        while(int(input("Ingrese un numero del 1 al 100 para adivinar: \n")) != numero_adivinar):
            os.system("cls")
            print("El número no es correcto, vuelve a intentar\n")
        print("Felicidades, adivinaste el numero!")

#EJ7
def agregar_producto(lista_compra):
    producto_a_agregar = input("Introduzca el producto que desea agregar a la lista de compras: ")
    while producto_a_agregar in lista_compra:
       producto_a_agregar = input("El producto ya se encuentra en la lista, por favor agregue un producto distinto aquí: ")
    lista_compra.append(producto_a_agregar)
    return lista_compra


def main():
    #EJERCICIO 1
    str1 = "Hola"
    str2 = "Hola, me llamo"
    str3 = "Hola, me llamo Facundo" # ejemplo string mas largo
    cadena_mas_larga, largo_cadena = string_mas_largo(str1,str2,str3)
    print("Ejercicio 1\n"
          "El string mas largo es: {}. Cuenta con {} carácteres.".format(cadena_mas_larga,largo_cadena) + "\n")

    #EJERCICIO 2
    lista = [1,2,3,4,5]
    print("Ejercicio 2\n"
          "La suma de los elementos de la lista es: {}".format(suma(lista)) + "\n")

    #EJERCICIO 3
    numero1 = 3
    numero2 = 24
    print("Ejercicio 3\n"
          "{} es impar? {}".format(numero1,es_impar(numero1)))
    print("{} es impar? {}".format(numero2,es_impar(numero2)) + "\n")

    #EJERCICIO 4
    print(str(decision()) + "\n")

    #EJERCICIO 5
    texto_minus = "Hola, como estas?"
    print(a_mayus(texto_minus))

    #EJERCICIO 6
    adivinar(88)

    #EJERCICIO 7
    lista_compra = ["Queso", "Pan", "Agua", "Zapallo"]
    print(agregar_producto(lista_compra))

if __name__ == "__main__":
    main()