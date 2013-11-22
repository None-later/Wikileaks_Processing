from get_entity import *
import json
a=['/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad00-03.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad03-06.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad06-08.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad08-10.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad80-90.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad90-95.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy Islamabad95-00.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy New Delhi03-06.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy New Delhi06-08.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy New Delhi08-10.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy New Delhi80-90.txt','/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/wiki Embassy New Delhi95-00.txt']
for name in a:	
	cables=readcables(name)
	city=[]
	i=1
	for cable in cables:
	    pos=parts_of_speech(cable)
	    entity=find_entities(pos)
	    city.append(entity)
	    print "processing  cable",i
	    i=i+1
	entity=[]
	for i in city:
	    for j in i:
		entity.append(j)
	pg=dict((i,entity.count(i)) for i in entity)
	gp=sorted(pg.items(),key=lambda (k,v):v)
	f=open(name+"count","a+")
	for i in range(len(gp)):
	    c=gp[i][0]+"::"+str(gp[i][1])
	    f.write(c)
	    f.write("\n")
	f.close
	    

