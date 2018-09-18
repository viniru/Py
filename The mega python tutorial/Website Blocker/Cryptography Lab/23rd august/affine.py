
with open('input.txt', 'r') as myfile:
  str = myfile.read()
#str = input("Enter a string : ")
a = int(input("Enter a key coprime to 26:"))
b = int(input("Enter another key "))
output = open("OutputAffine.txt","w")
outstr = ""
for c in str:
    if c.isalpha():
        if(ord(c) > 96):
            sub = 97
        else:
            sub = 65

        e = ((a*(ord(c) - sub) + b ) % 26)+sub
        outstr += chr(e)

    else:
        if c == '\n':
            output.write(outstr)
            outstr = ""
        outstr += c;
