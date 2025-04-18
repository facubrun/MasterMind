def potencia(numero,base=2): # predefinido base 2
    resultado = numero
    for i in range(1,base):
        resultado *= numero
    return resultado

def main():
    print(potencia(2))
    print(potencia(2,2))
    print(potencia(4,5)) # 4^2
    print(potencia(3,9)) # 3^9

if __name__ == "__main__":
    main()