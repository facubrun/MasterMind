import random

titulo = "\nJuego misión Marvel"
print(titulo)
print("-" * len(titulo) + "\n"
      "Te levantas en una nave espacial sin saber como llegaste ahí, en frente tenes una pantalla con un mensaje y\n"
      "dos opciones debajo. El mensaje dice que debes completar una misión para salvar al mundo de una fuerza\n"
      "superior de otro universo llamado Apache, está misión la deben completar en conjunto Spiderman y Ironman,\n"
      "tú debes elegir ser uno de ellos, antes de empezar te advierten que las personas del otro universo tienen\n"
      "el mismo aspecto fisico que las del nuestro."
      "\n")

opcion = input("[Opción A - SPIDERMAN] | [Opción B IRONMAN]\n")

if opcion == "A":
    print("Te dejan el traje en un armario, te lo pones?\n")
    opcion = input("[Opcion A - SI] | [Opción B - NO]\n")

    if opcion == "A":
        print("Al salir por la puerta de la habitación de la nave, Apache-Thor te ve con el traje y te mata\nFIN")

    elif opcion == "B":
        numero_groot = random.randint(1,77)
        papel_secreto = False
        print("Sales de la habitación con ropa de recluso y Apache-Thor no te reconoce sin el traje de Spiderman\n"
              "Te permite avanzar por un pasillo largo, al final se ven 2 puertas. En una de ellas ves a Groot y\n"
              "en la otra a Marry Jane que te saluda. A cual entras?\n")
        opcion = input("[Opción A - Groot] | [Opción B Marry Jane]\n")

        if opcion == "A":
            print("Groot te dice: 'yo soy groot, yo soy groot, yo soy groot' y te da un lapiz y un papel\n"
                  "que tiene la siguiente operación: 11 * {}".format(numero_groot) + "\n")
            opcion = int(input("¿Cual es el resultado?\n"))

            if opcion == 11 * numero_groot:
                print("Groot te indica por cual de las dos puertas que tienen delante debes entrar y como acertaste,\n"
                      "cree que eres muy inteligente y decide no darte un codigo que tiene guardado en otro papel.\n")

            else:
                print("Groot te indica por cual de las dos puertas que tienen delante debes entrar y como fallaste,\n"
                      "decide darte un codigo secreto que tiene guardado en otro papel.\n")
                papel_secreto = True

            print("Entras por la puerta y tienes en frente una maquina con un teclado, se bloquea la puerta y tenes\n"
                  "10 segundos para poner un codigo. Que haces?\n")

            if papel_secreto:
                opcion = input("[Opcion A - Escribó el codigo que me dió Groot] | [Opcion B - Escribo 1234 porque no confió en Groot]\n")

                if opcion == "A":
                    print("Resulta que es Groot de nuestro universo y el codigo es correcto, salvas a la humanidad\nFIN")

                elif opcion == "B":
                    print("No es el codigo dado por Groot, por lo que explota la nave y mueres\nFIN")

        elif opcion == "B":
            print("Resulta que es una trampa y es Apache-Marry Jane, por lo que al entrar te sorprende\n"
                  "AntMan de espaldas y te mata\nFIN")

elif opcion == "B":
    print("Te pones el traje que estaba al lado de la puerta y sales por ella.\n"
         "Al salir por la puerta de la habitación de la nave, Apache-Thor te ve y no sabe cual IronMan eres,\n"
         "por lo que decide preguntarte cual es su universo. Que respondes?\n")
    opcion = input("[Opción A - Respondes: 'el de siempre'] | [Opción B Sales corriendo]\n")

    if opcion == "A":
        print("Apache-Thor queda confundido con tu respuesta y te deja pasar\n"
              "Tienes dos puertas y no ves nada al otro lado, por cual entras?\n")
        opcion = input("[Opcion A - Por la derecha] | [Opcion B - Por la izquierda]\n")

        if opcion == "A":
            print("Caes directamente al vacío ya que es una puerta de otro universo que tiene esa funcionalidad. Mueres\nFIN")

        elif opcion == "B":
            papel_secreto = False
            print("Entras y te encuentras con Apache-Groot delante de una única puerta, que haces?\n")
            opcion = input("[Opción A - Pelear contra él] | [Opción B - Apartarlo y pasar a la siguiente puerta]\n")
            if opcion == "A":
                print("Lo derrotas facilmente y ves que tiene un papel con un codigo, lo tomas y pasas por la puerta.\n")
            print("Al pasar por la puerta, está se bloquea y frente a tí hay una pantalla con un teclado, te dan 10\n"
                  "segundos para que pongas un codigo. Que haces?\n")

            if papel_secreto:
                opcion = input("[Opcion A - Pongo el codigo que está en el papel] | [Opcion B Pongo cualquier otro codigo]\n")
                if opcion == "A":
                    print(
                        "Resulta que el codigo es correcto, salvas a la humanidad\nFIN")
                elif opcion == "B":
                    print("No es el codigo correcto, por lo que explota la nave y mueres\nFIN")



    elif opcion == "B":
        print("Tras una larga lucha, un hachazo(usa otra herramienta) de Apache-Thor rompe parte de la nave y\n"
            "ambos mueren al caer en el espacio.\nFIN")

else:
    print("No elegiste ninguna opción, mueres\nFIN")




