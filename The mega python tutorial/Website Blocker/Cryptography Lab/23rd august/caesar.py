#str = input("Enter some string :")
fileout = open("outputCaesar.txt","w")
k = int(input("Enter the key :"))
strout = ""
listOfLines = []
with open("input.txt","r") as f:
    while(True):
        c = f.read(1)
        if not c:
            break;
        else:
            if c.isalpha():
                if(ord(c) > 96):
                    sub = 97
                else:
                    sub = 65
                strout += chr(sub + (ord(c) - sub + k)%26)

            else:
                if c == '\n' :
                    fileout.write(strout)
                    strout = ""
                strout += c
