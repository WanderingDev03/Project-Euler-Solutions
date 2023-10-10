def isPrime(n):
    i = 1
    while True:
        i += 1
        if n == i:
            break
        if n % i == 0:
            return False
    return True

def main():
    n = 600851475143
    i = 1
    l = list()
    while True:
        i += 1
        while True:
            if (isPrime(i) and n % i == 0):
                n/=i
                l.append(i)
                continue
            break    
        if (n == 1):
            break
    print(max(l))
            
if __name__ == "__main__":
    main()
