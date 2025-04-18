print("Voy a la cocina")
print("Abro la heladera")
hay_leche = input("¿Hay leche? (S/N) ")
hay_cafe = input("¿Hay café? (S/N) ")

if hay_leche != "S" or hay_cafe != "S":
    print("Voy al super")
    if(hay_leche != "S"):
        print("Compro leche")
    if(hay_cafe != "S"):
        print("Compro café")
print("Hago el café con leche")
