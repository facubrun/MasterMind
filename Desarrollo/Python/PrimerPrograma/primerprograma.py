a = int(input("Elige tu primer numero:"))
b = int(input("Elige tu segundo numero:"))
c = int(input("Elige tu tercer numero:"))
print("El maximo entre {}, {} y {} es {}, mientras que el minimo es {}".format(a,b,c,
                                                                               max(a,b,c),
                                                                               min(a,b,c)))