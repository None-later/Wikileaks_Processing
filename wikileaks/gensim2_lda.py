import codecs 
import re
import nltk
import gensim
import logging
import glob
import os
from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
stoplist =['I','a','an','as','at','by','he','his','me','or','thou','us','who','against','amid','amidst','among','amongst','and','anybody','anyone','because','beside','circa','despite','during','everybody','everyone','for','from','her','hers','herself','him','himself','hisself','idem','if','into','it','its','itself','myself','nor','of','oneself','onto','our','ourself','ourselves','per','she','since','than','that','the','thee','theirs','them','themselves','they','thine','this','thyself','to','tother','toward','towards','unless','until','upon','versus','via','we','what','whatall','whereas','which','whichever','whichsoever','whoever','whom','whomever','whomso','whomsoever','whose','whosoever','with','without','ye','you','you-all','yours','yourself','yourselves','aboard','about','above','across','after','all','along','alongside','although','another','anti','any','anything','around','astride','aught','bar','barring','before','behind','below','beneath','besides','between','beyond','both','but','concerning','considering','down','each','either','enough','except','excepting','excluding','few','fewer','following','ilk','in','including','inside','like','many','mine','minus','more','most','naught','near','neither','nobody','none','nothing','notwithstanding','off','on','opposite','other','otherwise','outside','over','own','past','pending','plus','regarding','round','save','self','several','so','some','somebody','someone','something','somewhat','such','suchlike','sundry','there','though','through','throughout','till','twain','under','underneath','unlike','up','various','vis-a-vis','whatever','whatsoever','when','wherewith','wherewithal','while','within','worth','yet','yon','yonder']
class MyCorpus(object):
    def __iter__(self):
        for line in open(temporary):
            print "temporary is "+temporary
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())
os.chdir("bodyonlyoutput/")
folderlist=['bodyonly66_80','bodyonly80_90','bodyonly90_95','bodyonly95_00','bodyonly00_01','bodyonly01_02','bodyonly02_03','bodyonly03_04','bodyonly04_05','bodyonly05_06','bodyonly06_07_1','bodyonly06_07_2','bodyonly06_07_3','bodyonly06_07_4','bodyonly06_07_5','bodyonly06_07_6','bodyonly06_07_7','bodyonly06_07_8','bodyonly06_07_9','bodyonly06_07_10','bodyonly06_07_11','bodyonly06_07_12','bodyonly08_09_1','bodyonly08_09_2','bodyonly08_09_3','bodyonly08_09_4','bodyonly08_09_5','bodyonly08_09_6','bodyonly08_09_7','bodyonly08_09_8','bodyonly08_09_9','bodyonly08_09_10','bodyonly08_09_11','bodyonly08_09_12','bodyonly07_08_1','bodyonly07_08_2','bodyonly07_08_3','bodyonly07_08_4','bodyonly07_08_5','bodyonly07_08_6','bodyonly07_08_7','bodyonly07_08_8','bodyonly07_08_9','bodyonly07_08_10','bodyonly07_08_11','bodyonly07_08_12','bodyonly09_10_1','bodyonly09_10_2','bodyonly09_10_3','bodyonly09_10_4','bodyonly09_10_5','bodyonly09_10_6','bodyonly09_10_7','bodyonly09_10_8','bodyonly09_10_9','bodyonly09_10_10','bodyonly09_10_11','bodyonly09_10_12']
#'bodyonly66_80','bodyonly80_90','bodyonly90_95','bodyonly95_00','bodyonly00_01','bodyonly01_02',
for folder in folderlist:
	print folder
	for files in glob.glob(folder+"/"+"*"):
		fi=codecs.open(files, 'r', encoding='utf-8')
		f=fi.read()
		fi.close()		
		f=f.split("\n")
		documents=[]
		for index,line in enumerate(f):
			if index!=len(f):
				documents.append(line)
		texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
 		all_tokens = sum(texts, [])
		tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
		texts = [[word for word in text if word not in tokens_once] for text in texts]		
		dictionary = corpora.Dictionary(texts)
		corpus = [dictionary.doc2bow(text) for text in texts]
		dictionary.compactify()
		model = gensim.models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=5)	
		name=folder
		name=folder.replace("bodyonly",'')
		name2=files
		name2=files.replace(name,'')
		name2=name2.replace("bodyonly/","")
		for i in range(0,5):
#			print model.print_topic(i, topn=10)	
			fi=codecs.open("log"+name+"/"+name2, 'a+', encoding='utf-8')
#		f=fi.read()
			fi.write(model.print_topic(i, topn=10))
			fi.write("\n")
			fi.close()	
		print folder+files
	
	
	
#	
#	
#	
	
#		print files
#		global temporary
#		temporary=files
#		dictionary = corpora.Dictionary(line.lower().split() for line in open(temporary))
#### remove stop words and words that appear only once
###
#		stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
#			    if stopword in dictionary.token2id]
#		once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
#		dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
#		dictionary.compactify() # remove gaps in id sequence after words that were removed
#		corpus = MyCorpus()
#		tfidf = models.TfidfModel(corpus)
#		corpus_tfidf = tfidf[corpus]
#		#lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20)
#		#corpus_lsi = lsi[corpus_tfidf]

#		#lsi.save('/tmp/model.lsi') # same for tfidf, lda, ...
#		#lsi = models.LsiModel.load('/tmp/model.lsi')
#		################### latent semantic Indexing
#		model = gensim.models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=5)
#		temporary=''
