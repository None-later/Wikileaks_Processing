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


#os.chdir("/media/New Volume/split/time_frame/new95-00/")
t=['09_10_3']
#'06_07_1','06_07_2','06_07_3','06_07_4','06_07_5','06_07_6','06_07_7','06_07_8','06_07_9','06_07_10','06_07_11','06_07_12','07_08_1','07_08_2','07_08_3','07_08_4','07_08_5','07_08_6','07_08_7','07_08_8','07_08_9','07_08_10','07_08_11','07_08_12','08_09_1','08_09_2','08_09_3','08_09_4','08_09_5','08_09_6','08_09_7','08_09_8','08_09_9','08_09_10','08_09_11','08_09_12','09_10_1','09_10_2','05_06','06_07','07_08','08_09','09_10']
for l in t:
	os.chdir("new"+l+"/")
	for files in glob.glob("*"):
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
#		f=open("../count"+l+"/"+files,"r")
		
		f=open("../count"+l+"/"+files,"w")
		for i in range(len(gp)):
			c=gp[i][0]+"::"+str(gp[i][1])
			f.write(c)
			f.write("\n")
		f.close
	os.chdir("..")
		    

