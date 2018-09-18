import glob2
from datetime import datetime
timestamp = datetime.now()
currentTime = timestamp.strftime("%Y-%m-%d-%H-%M-%S-%MS")
filenames = glob2.glob("*.txt");
with open(str(currentTime)+".txt","w") as newfile:
    for file in filenames:
        one = open(file,"r")
        newfile.write(one.read())
