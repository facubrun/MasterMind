
num_elegido = int(input("Introduzca el numero a multiplicar:"))

for n in range(1,11):
    if n % 2 == 0: #Devuelve solo la multiplicacion con multiplos de 2
        print("{} x {} = {}".format(num_elegido, n, num_elegido * n))
