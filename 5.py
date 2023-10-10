from math import lcm  
    
def main():
    l = range(1, 21)
    lcm_val=lcm(l[0],l[1])
 
    for i in range(2,len(l)):
        lcm_val=lcm(lcm_val,l[i])
    print(lcm_val)

if __name__ == "__main__":
    main()
