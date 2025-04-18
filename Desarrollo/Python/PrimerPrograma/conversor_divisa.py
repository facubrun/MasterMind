
dolar_euro = 0.91
libra_euro = 1.18

opcion = int(input("Elige que conversion quieres hacer:\n"
                   "1. Dolar a Euro\n"
                   "2. Euro a Dolar\n"
                   "3. Libra a Euro\n"
                   "4. Euro a Libra\n"))

texto_user = "Ingrese la cantidad de {} a convertir:"
if opcion == 1:
    dolares = float(input(texto_user.format("dolares")))
    print("\n{} dolares son {} euros.".format(dolares, dolares * dolar_euro))

elif opcion == 2:
    euros = float(input(texto_user.format("euros")))
    print("\n{} euros son {} dolares.".format(euros, euros / dolar_euro))

elif opcion == 3:
    libras = float(input(texto_user.format("libras")))
    print("\n{} libras son {} euros.".format(libras, libras * libra_euro))

elif opcion == 4:
    euros = float(input(texto_user.format("euros")))
    print("\n{} euros son {} libras.".format(euros, euros / libra_euro))

else:
    print("No eligio ninguna opción válida.")