import nltk
from nltk.book import *
from nltk.corpus import brown
from nltk import word_tokenize


def lexical_diversity(text):
	return len(set(text))/len(text)

def percentage(count, total):
	return 100 * count/total
	
fdist = FreqDist(text1)

def long_words(text,length):
        V = set(text)
        lw = [w for w in V if len(w) > length]
        return sorted(lw) 

def func():
        from nltk.corpus import brown
        brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
        tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
        print(tag_fd.most_common())

def eratag():
        f = open('eragon_para_a_tagger.txt').read()
        text = word_tokenize(f)
        return text

print(eratag())

  	
def mytagger():
        t0 = nltk.DefaultTagger('NN')
        t1 = nltk.UnigramTagger('eragon_pos_tag_corrige.txt', backoff=t0)
        t2 = nltk.BigramTagger('eragon_pos_tag_corrige.txt', backoff=t1)
        from pickle import dump
        output = open('t2.pkl', 'wb')
        dump(t2, output, -1)
        output.close()
