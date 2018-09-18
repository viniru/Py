correctPassword = "vin@123"
name = input("enter your name : ")
surname = input("enter your surname : ")
password=input("enter the password :")

while correctPassword != password:
    password=input("wrong password ! Enter the correct passord ")

print('hi %s %s logged in'%(name,surname))
