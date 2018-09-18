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

def multIn(a,m):
    global x;
    extendedEcli(a,m)
    inverse = (x%m + m)%m
    return inverse



def chineseMethod():
    n = int(input("How many equations do you want to enter  ?"))
    equa = []
    M = 1
    for i in range(0,n):
        equa.append([int(_) for _ in input("Enter the {0}th equation :".format(i+1)).split(" ")])
        M = M * equa[i][1]

    x = 0;
    for i in range(0,n):
        b = M/equa[i][1]
        print(b,"  this is b \n")
        bb = multIn(b,equa[i][1])
        print(bb," This is bb\n")
        x = (x % M+ ( equa[i][0]*b*bb ) % M)%M
    x = x % M

    print("The value of x is ",x)

chineseMethod()
