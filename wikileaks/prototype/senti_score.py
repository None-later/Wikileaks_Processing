from sentiwn import *
import nltk

def readfile(name):
    f=open(name,'r')
    f=f.readlines()
    return f
file_name = "dump/SentiWordNet_3.0.0_20130122.txt"
sw = SentiWordNet(file_name)
##p,n=sw.get_score("good")
f=open("entities/pakentity.txt")
g=open("result.txt","a+")
entities=f.readlines()
for entity in entities:
    entity=entity.strip("\n").lower()
    tp=0.0
    tn=0.0
    count=1
   
    for cable in readfile('files used/cleanpaki.txt'):
        #print "analysing cable ....."
        sentences = nltk.sent_tokenize(cable)
        #tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
        for sentence in sentences:
            tokenized=nltk.word_tokenize(sentence)
            #print tokenized
            if (entity in tokenized):
                #print "found !!!"
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
                        
                    
        
            
        
    
    #pos_tags  = [nltk.pos_tag(sentence) for sentence in tokenized]



