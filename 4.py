def isPalindrome(n: str):
    length = len(n)
    if (length % 2 == 1):
        return False
    i = 0
    if (n[:(length // 2)] == (n[(length // 2):])[::-1]):
        return True
        
def main():
    palindromes = list()
    for i in range(100, 1000):
        for j in range(100, 1000):
            if isPalindrome(str(j*i)):
                palindromes.append(j*i)
    print(max(palindromes))
    
if __name__ == "__main__":
    main()
