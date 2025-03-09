print("Bienvenido a mi conversor de Fahrenhei a Celsius")
grados_fahrenheit = int(input("Ingrese los grados fahrenheit para hacer la conversión: "))
grados_celsius = ((grados_fahrenheit - 32)*5)/9
print(str(grados_fahrenheit) + "°F son "
      + str(grados_celsius) + "°C")