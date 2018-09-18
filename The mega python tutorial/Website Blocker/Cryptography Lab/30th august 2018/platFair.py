key = input("Enter a key for play fair encryption :")
flag = 0
for c in key:
    if c.isdigit():
        flag = 1
        break

if flag == 0 :
    m = 5
    n = 5
else:
    m = 6
    n = 6

mat = [[0]*n]*m

chars = []

keySet = set([])
for i in key:
    if i.isalnum() == True:
        if keySet.__contains__(i) == False:
            chars.append(i)
            keySet.add(i)


for i in range(97,123):
    if keySet.__contains__(chr(i)) == False:
        chars.append(chr(i))

if flag == 1:
    for i in range(48,58):
        if keySet.__contains__(chr(i)) == False:
            chars.append(chr(i))

k = 0
for i in range(0,m):
    for j in range(0,n):
        #print(chars[k]+" ",end='')
        mat[i][j] = chars[k]
        k += 1
    #print("\n")

def columnNrow(ele):
    i=0
    j=0
    m = mat.__len__()
    n = mat[0].__len__()
    for i in range(m):
        for j in range(n):
            if ele == mat[i,j]:
                return [i,j]

def encrypt():
    file = open("inputplayfair.txt")
    str = file.read()
    newstr = ""
    pairs = [[0]*2]
    i = 0
    while i < len(str) - 1:
        if str[i] == str[i+1] :
            pairs.append([str[i],'x'])
        pairs.append(str[i],str[i+1])
        i = i + 2

    if(i == len(str))
        pairs.append([str[i],'x'])

    ecr = ""

    for T in pairs:
        f = columnNrow(T[0])
        s = columnNrow(t[1])

        if f[0] == s[0]:
            ecr += mat [f[1]] [(f[1] + 1) % mat[0].__len__()]
            ecr += mat [s[1]] [(s[1] + 1) % mat[0].__len__()]

        elif f[1] == s[1]:
            ecr += mat [f[0]] [(f[0] + 1) % mat[0].__len__()]
            ecr += mat [s[0]] [(s[0] + 1) % mat.__len__()]

        else:
            
