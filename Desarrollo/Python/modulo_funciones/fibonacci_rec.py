def fibonacci_rec(n):
    if n <= 1:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

def main():
    for i in range(10):
        print(fibonacci_rec(i))

if __name__ == "__main__":
    main()