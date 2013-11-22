###remove stopwords
import nltk
f=open("stop.txt","r")
f=f.readlines()
stop=[]
for i in f:
    stop.append(i.strip("\n").strip("\r"))
stop=set(stop)
f=open("small/wikidelhi.txt","r")
f=f.readlines()
new=open("cleandelhi.txt","a+")
z=0
for line in f:
    print z
    z=z+1
    line=line.lower().strip("()")
    line_tokens=nltk.word_tokenize(line)
    for word in line_tokens:
        if(word not in stop):
            new.write(" "+word+" ")
    new.write("\n")
            
        
    
