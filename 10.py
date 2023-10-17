def isPrime(n: int) -> bool:
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, n, 2):
        if n % i == 0:
            return False
    return True

def main():
    N = 2_000_000
    is_prime = [1 for num in range(N)]
    is_prime[0] = 0
    is_prime[1] = 0

    def set_prime(num):
        for x in range(num*2, N, num):
            is_prime[x] = 0

    for num in range(N):
        if is_prime[num] == 1:
            set_prime(num)

    primes = [num for num in range(N) if is_prime[num]]
    print(sum(primes))

if __name__ == "__main__":
    main()
