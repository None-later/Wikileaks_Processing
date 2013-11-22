import json
import nltk
#embassy=raw_input("enter the embassy u want\n")
f=open("/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/delhi/Embassy Baghdad90-95","r")
raw=open("/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/delhi/wiki Embassy Baghdad90-95","a+")
text=f.readlines()
c=0
for line in text:
    cable=json.loads(line)
    raw.write(cable['body'].strip("\n").encode('ascii', 'ignore'))
    raw.write("\n")
f.close
raw.close
