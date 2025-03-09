from random import randint

print("Bienvenido a adivina el número")
num_ganador = randint(1,10)
num_usuario = int(input("Intenta adivinar un numero del 1 al 10: "))
if num_usuario == num_ganador:
    print("Felicidades, acertaste")

if num_usuario < 1 or num_usuario > 10:
    print("El número elegido no es válido")

print("El número ganador era {}".format(num_ganador))
