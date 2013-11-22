entity=[]
for i in city:
    for j in i:
        entity.append(j)
pg=dict((i,entity.count(i)) for i in entity)
gp=sorted(pg.items(),key=lambda (k,v):v)
f=open("count_islamabad.txt","a+")
for i in range(len(gp)):
    f.write(gp[i][0]+"::"+str(gp[i][1]))
    f.write("\n")
f.close
