import math
def gcd(a,b):
    if b == 0 :
        return a
    return(gcd(b,a%b))


def generator(n):
    znstar = []
    order = {}
    for i in range(1,n):
        if gcd(i,n) == 1:
            znstar.append(i)


    znstarsize = len(znstar);
    print(znstar)
    print("size : ",znstarsize)
    znstar.remove(1)
    flag = False
    for i in znstar:
        for j in range(1,znstarsize+1):
            if(math.pow(i,j) % n == 1):
                print("The generator is ",i)
                flag = True
                break
        if(flag):
            break

n = int(input("\nEnter an element : "))
generator(n)
