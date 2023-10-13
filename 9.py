from math import sqrt

def main():
    for a in range(1, 1001):
        for b in range(1, 1001):
            a_2 = a**2
            b_2 = b**2
            c_2 = a_2+b_2
            if ((c := sqrt(c_2)) % 1 == 0) and (((a := sqrt(a_2))) +  (b := (sqrt(b_2))) + c) == 1000:
                print(a*b*c)
                print(a, b, c)
                return
               
if __name__ == "__main__":
    main()
    