def isPrime(n: int):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    i = 1
    while True:
        i += 1
        if (n == i):
            return True
        
        if (n % i == 0):
            return False
            
    return True

def nthPrime(n: int):
    i = 0
    n1 = 0
    while True:
        i += 1
        if isPrime(i):
            n1 += 1
        if (n1 == n):
            return i
        if (i == 10000000):
            break

def main():
    print(nthPrime(10001))
        
if __name__ == "__main__":
    main()