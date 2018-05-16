import nltk
from nltk.book import *
from nltk.corpus import brown
from nltk import word_tokenize
from pickle import dump 

f = open('eragon.txt').read()
h = word_tokenize(f)


def lexical_diversity(text):
	return percentage(len(set(text)),len(text))

def percentage(count, total):
	return 100 * count/total

def long_words(text,length):
        V = set(text)
        lw = [w for w in V if len(w) > length]
        return sorted(lw) 
		
def eragon_diversite():
	f = open('eragon.txt').read()
	f = word_tokenize(f)
	print(lexical_diversity(f))

  	
def mytagger():
        sents = brown.tagged_sents(categories ='fiction')
        size = int(len(sents) * 0.9)
        train_sents = sents[:size]
        test_sents = sents[size:]
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger(train_sents, backoff=t0)
        t2 = nltk.BigramTagger(train_sents, backoff=t1)
        print(t2.evaluate(test_sents))
        print(t2.evaluate(brown.tagged_sents(categories='news')))

def myFreqDist(text,length,occ):
        fdist = FreqDist(text)
        return sorted(w for w in set(text) if len(w) > length and fdist[w] > occ)

fdist = FreqDist(long_words(h,4))
fdist.most_common(10)

fdist2 = FreqDist(long_words(text4,4))
fdist2.most_common(10)
