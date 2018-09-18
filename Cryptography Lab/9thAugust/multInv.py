import math
x = 0;
y = 0;
def extendedEcli(a,b):
    global x,y
    if b==0:
        x = 1
        y = 0

    else:
        extendedEcli(b,a%b);
        x , y = y , x - int(math.floor(a/b)) * y;

def multIn():
    global x;
    a = 7
    m = 2
    extendedEcli(a,m)
    inverse = (x%m + m)%m
    print("The multiplicative inverse of {} is :",inverse)

multIn()
