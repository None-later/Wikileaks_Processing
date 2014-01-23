from sentiwn import *
import nltk
import os
import glob
def readfile(name):
    f=open(name,'r')
    f=f.readlines()
    return f
file_name = "dump/SentiWordNet_3.0.0_20130122.txt"
sw = SentiWordNet(file_name)
##p,n=sw.get_score("good")
yearlist=['66_80','80_90','90_95','95_00','00_01','01_02','02_03','03_04','04_05','05_06','06_07_1','06_07_2','06_07_3','06_07_4','06_07_5','06_07_6','06_07_7','06_07_8','06_07_9','06_07_10','06_07_11','06_07_12','08_09_1','08_09_2','08_09_3','08_09_4','08_09_5','08_09_6','08_09_7','08_09_8','08_09_9','08_09_10','08_09_11','08_09_12','07_08_1','07_08_2','07_08_3','07_08_4','07_08_5','07_08_6','07_08_7','07_08_8','07_08_9','07_08_10','07_08_11','07_08_12','09_10_1','09_10_2','09_10_3','09_10_4','09_10_5','09_10_6','09_10_7','09_10_8','09_10_9','09_10_10','09_10_11','09_10_12']
os.chdir("count/")
for year in yearlist:
	for files in glob.glob("entity"+year+"/"+"*"):
		#print files
		f=open(files,"r")
		nameoffile=files
		nameoffile=nameoffile.replace("entity"+year+"/","")
		print nameoffile
		g=open("result"+year+"/"+nameoffile,"a+")
		entities=f.readlines()
		tp=0.0
		tn=0.0
		count=1
		for entity in entities:
		    entity=entity.strip("\n")
		    print entity
		    for cable in readfile('bodyonly'+year+'/'+nameoffile):
#		    	print cable
			#print "analysing cable ....."
			sentences = nltk.sent_tokenize(cable)
			#tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
			for sentence in sentences:
			    tokenized=nltk.word_tokenize(sentence)
			    #print tokenized
			    if (entity in tokenized):
				print "found !!!"
				pos_tags=nltk.pos_tag(tokenized)
				for w,adj in pos_tags:
				    if adj=='JJ':
				        count=count+1
				        #print "\t",w,adj
				        p,n=sw.get_score(w)
				        #print "\t\t",p,n
				        tp=tp+p
				        tn=tn+n
					print round(tp/count,3),round(tn/count,3)
					res=""
					res=res+str(round(tp/count,3))+str(round(tn/count,3))
					g.write(res)
                        
                    
        






#f=open("entity","r")
#g=open("result.txt","a+")
#entities=f.readlines()
#tp=0.0
#tn=0.0
#count=1
#for entity in entities:
#    entity=entity.strip("\n")
#    print entity
#    for cable in readfile('new/baghdad/wiki Embassy Baghdad90-95'):
#    	print cable
#        #print "analysing cable ....."
#        sentences = nltk.sent_tokenize(cable)
#        #tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
#        for sentence in sentences:
#            tokenized=nltk.word_tokenize(sentence)
#            #print tokenized
#            if (entity in tokenized):
#                print "found !!!"
#                pos_tags=nltk.pos_tag(tokenized)
#                for w,adj in pos_tags:
#                    if adj=='JJ':
#                        count=count+1
#                        #print "\t",w,adj
#                        p,n=sw.get_score(w)
#                        #print "\t\t",p,n
#                        tp=tp+p
#                        tn=tn+n
#			print round(tp/count,3),round(tn/count,3)
#res=""
#res=res+str(round(tp/count,3))+str(round(tn/count,3))
#g.write(res)
#                        
#                    
        
            
        
    
    #pos_tags  = [nltk.pos_tag(sentence) for sentence in tokenized]



