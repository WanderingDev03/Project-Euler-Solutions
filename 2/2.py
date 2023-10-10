from fibonacci import fibonacci

def main():
    i = 0
    sum = 0
    while True:
        i += 1
        fib = fibonacci(i)
        if (fib > 4_000_000):
            break
        if fib % 2 == 0:
            sum += fib
        print(fib)
    print("\n"+str(sum))

if __name__ == "__main__":
    main()
