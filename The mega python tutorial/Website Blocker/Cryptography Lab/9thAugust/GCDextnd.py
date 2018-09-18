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

a = 4;
b = 8;
extendedEcli(a,b)
print(x*a+y*b)
