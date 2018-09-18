import math
x = 0;
y = 0;
def extendedEcli(i,j):
    global x,y
    if j==0:
        x = 1
        y = 0

    else:
        extendedEcli(j,i%j);
        x , y = y , x - int(math.floor(i/j)) * y;

def multIn(a):
    global x;
    m = 26
    extendedEcli(a,m)
    return((x%m + m)%m)

str = input("Enter the encrypted text : ")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
inverse = multIn(a)
for c in str :
    if c.isalpha():
        if(ord(c) > 96):
            sub = 97
        else:
            sub = 65
        print((chr) ((inverse *( ( ord(c)-sub - b) % 26 ) + 26 ) % 26 + sub),end='')

    else:
        print(c,end='')
