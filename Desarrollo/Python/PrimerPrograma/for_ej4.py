
numeros_introducidos = input("Introduzca los números a agregar separados por coma: ")
numeros_usuario = [int(numero) for numero in numeros_introducidos.split(",")]

min_numero = numeros_usuario[0]
max_numero = numeros_usuario[0]

for numero in numeros_usuario[1:]: # Empieza desde el indice 1 hasta el final
    if min_numero > numero:
        min_numero = numero

    if max_numero < numero:
        max_numero = numero

print("El minimo es {}\n".format(min_numero) +
      "El maximo es {} ".format(max_numero))