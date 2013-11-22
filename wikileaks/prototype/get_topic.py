import nltk
import gensim
import logging
from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
stoplist = set('for a of the and to in india indian delhi '.split())
class MyCorpus(object):
    def __iter__(self):
        for line in open('cleandelhi.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

# collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for line in open('cleandelhi.txt'))
### remove stop words and words that appear only once
##
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
corpus = MyCorpus()
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20)
corpus_lsi = lsi[corpus_tfidf]

lsi.save('/tmp/model.lsi') # same for tfidf, lda, ...
lsi = models.LsiModel.load('/tmp/model.lsi')
################### latent semantic Indexing
model = gensim.models.ldamodel.LdaModel(corpus, id2word=dictionary, num_topics=20)
