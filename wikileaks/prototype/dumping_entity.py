f=open("demo.txt","a+")
for i in city:
    for j in i:
        f.write(j)
        f.write("--")
    f.write("\n")
    f.write("*************************************************************")
        
