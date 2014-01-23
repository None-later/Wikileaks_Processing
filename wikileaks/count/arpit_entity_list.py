import json
import nltk
import glob
import os
import codecs
def readcables(filename):
    text=open(filename,"r")
    lines=text.readlines()
    return lines
def score(cable):
    scores= nltk.probability.FreqDist(cable).keys()
    return scores
    
def parts_of_speech(corpus):
    "returns named entity chunks in a given text"
    sentences = nltk.sent_tokenize(corpus)
    tokenized = [nltk.word_tokenize(sentence) for sentence in sentences]
    pos_tags  = [nltk.pos_tag(sentence) for sentence in tokenized]
    return nltk.batch_ne_chunk(pos_tags, binary=True)

def find_entities(chunks):
    "given list of tagged parts of speech, returns unique named entities"

    def traverse(tree):
        "recursively traverses an nltk.tree.Tree to find named entities"
        entity_names = []
    
        if hasattr(tree, 'node') and tree.node:
            if tree.node == 'NE':
                entity_names.append(' '.join([child[0] for child in tree]))
            else:
                for child in tree:
                    entity_names.extend(traverse(child))
    
        return entity_names
    
    named_entities = []
    
    for chunk in chunks:
        entities = sorted(list(set([word for tree in chunk
                            for word in traverse(tree)])))
        for e in entities:
            if e not in named_entities:
                named_entities.append(e)
    return named_entities

files='Embassy Cairo'
#os.chdir("/media/New Volume/split/time_frame/new95-00/")
#t=['05_06']
##,'05_06','06_07','07_08','08_09','09_10']
#for l in t:
#	os.chdir("new"+l+"/")
#	for files in glob.glob("*"):
cables=readcables(files)
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
f=open(files,"a+")
print(files)
for i in range(len(gp)):
    c=gp[i][0]+"::"+str(gp[i][1])
    f.write(c)
    f.write("\n")
f.close
#os.chdir("..")
		    

