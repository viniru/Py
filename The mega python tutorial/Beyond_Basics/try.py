temperatures = [10, -20, -289, 100]
def c_to_f(temperatures,path):
    with open(path,"w") as myfile:
        for t in temperatures:
            if t >= -273.15:
                f = t* 9/5 + 32
                myfile.write(str(f)+"\n")
c_to_f(temperatures,"myfile.txt")
