import math
def gcd(a,b):
    if b == 0 :
        return a
    return(gcd(b,a%b))


def order(n):
    znstar = []
    order = {}
    for i in range(1,n):
        if gcd(i,n) == 1:
            znstar.append(i)

    for i in znstar:
        t = 1
        while True:
            if math.pow(i,t) % n == 1 :
                order[i] = t;
                break
            t = t + 1;

    print(order)

n = int(input("Enter an element : "))
order(n)
