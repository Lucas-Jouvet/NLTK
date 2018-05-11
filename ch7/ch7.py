locs = [('Omnicom' , 'IN' , 'New York' ),( 'DDB Needham' , 'IN' , 'New York' ),( "Groupe Kaplan Thaler" , "IN" , "New York" ),( "BBDO South" , "IN" , "Atlanta" ),( 'Georgia-Pacific' , 'IN' , 'Atlanta' )]
query = [e1 for (e1, rel, e2) in locs if e2 == 'Atlanta']
print (query)

print("##")

import nltk, re , pprint

def ie_preprocess(document):
    phrase = nltk.sent_tokenise(document)
    phrase = [nltk.word_tokenize(sent) for sent in sentences]
    phrase = [nltk.pos_taag(sent) for sent in sentences]


print("#")

  	

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)
result.draw()

print("##")
grammar = r"""
NP: {<DT|PP\$>?<JJ>*<NN>} 
{<NNP>+}
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]

print(cp.parse(sentence))

print("#")
nouns = [("money", "NN"), ("market", "NN"), ("fund", "NN")]
grammar = "NP: {<NN><NN>}
cp = nltk.RegexpParser(grammar)
print(cp.parse(nouns))
