def fibonacci_iterativo(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2,n):
        suma = n1 + n2
        n1 = n2
        n2 = suma
    return n2

def main():
    for i in range(1,10):
        print(fibonacci_iterativo(i))

if __name__ == "__main__":
    main()