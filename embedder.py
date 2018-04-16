import spacy
from math import log
import numpy as np

EmbeddingLength = 50
vblist = ['VB', 'VBD', 'VBG', 'VBP', 'VBZ', 'RB', 'RBR', 'RBS', 'RP', 'WDT', 'WRB']
nlist = ['CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'PRP']

#add whatever else we need
#returns numpy array of embedding
#note that spacy has a 
def getWordEmbedding(word, normalized, POSTAG):
	

#sentence is a unicode string.
#enlp is a instance of spacy which has been loaded with
#an appropriate model. if in doubt, spacy.load('en') should be provided
def makeSentenceEmbeddings(sentence, enlp):
	doc = enlp(sentence)
	sentence = list(doc.sents)[0]
	vsb = None
	ns = None
	mainvb
	mainsub
	queue = [sentence.root, None]
	depth = 0
	while len(queue) > 0:
		if queue[0] == None:
			depth +=1
			queue.pop(0)
		for child in queue[0]:
			queue.append(child)
		tok = queue.pop(0)
		wemb = getWordEmbedding(tok.text, tok.lemm_, tok.tag_)
		factor = 1 / log(depth)
		if not tok.stop_:
			factor *= .2
		if tok.tag_ in vblist:
			if vbs = None:
				vbs = wemb
				mainvb = tok
			else:
				if not mainvb in tok.ancestors:
					factor *= .5
				vbs += (wemb * factor)
		elif tok.tag_ in nlist:
			if ns = None:
				ns = wemb
				mainsub = tok
			else:
				if not mainsub in tok.ancestors:
					factor *= .5
				ns += (wemb * factor)
	embedding = np.concatenate(ns, vsb)		
	return embedding
