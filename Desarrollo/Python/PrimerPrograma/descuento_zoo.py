edad = int(input("Ingrese su edad: "))
tipo_de_carnet = input("Ingrese su tipo de carnet (E/P/F/N): ")

if ((25 <= edad <= 35 and tipo_de_carnet == "E") or
        (edad <= 10) or
        (edad >= 65 and tipo_de_carnet =="P") or
        (tipo_de_carnet == "F")):
    print("Se aplica el descuento.")
else:
    print("No aplica descuento.")

