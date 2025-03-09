titulo = "Bienvenido al test sobre futbol"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Cuantas veces a la semana miras futbol?\n"
                "A. Casi nunca\n"
                "B. Miro el fin de semana\n"
                "C. No me pierdo ningún partido\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A,B y C")
    exit()

opcion2 = input("Pregunta 2: Jugas al futbol seguido?\n"
        "A. Nunca juego\n"
        "B. A veces juego con amigos\n"
        "C. Juego siempre que alguien me invita\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A,B y C")
    exit()

opcion3 = input("Pregunta 3: Te gustan otros deportes?\n"
        "A. Si, me interesan mas otros deportes además del futbol\n"
        "B. Si, aunque prefiero el futbol\n"
        "C. No, solo juego y miro futbol\n")

if opcion == "A":
    puntuacion += 0
elif opcion == "B":
    puntuacion += 5
elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones posibles son A,B y C")
    exit()

if puntuacion >= 25:
    print("Felicidades, sos fanatico del futbol")
elif puntuacion >= 15 :
    print("Te gusta el futbol")
else:
    print("No te gusta el futbol")
