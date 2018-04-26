import spacy
from math import log
import numpy as np

vblist = ['VB', 'VBD', 'VBG', 'VBP', 'VBZ', 'RB', 'RBR', 'RBS', 'RP', 'WDT', 'WRB']
nlist = ['CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'PRP']


# add whatever else we need
# returns numpy array of embedding
# note that spacy has a
def getWordEmbedding(word, normalized, POSTAG):
    return np.array([0.0] * 50)


# sentence is a unicode string.
# enlp is a instance of spacy which has been loaded with
# an appropriate model. if in doubt, spacy.load('en') should be provided
def makeSentenceEmbeddings(sentence, enlp):
    doc = enlp(sentence)
    sentence = list(doc.sents)[0]
    vsb = None
    ns = None
    queue = [sentence.root, None]
    depth = 2
    while len(queue) > 0:
        if queue[0] is None:
            depth += 1
            queue.pop(0)
            continue
        for child in queue[0].children:
            queue.append(child)
        tok = queue.pop(0)
        wemb = getWordEmbedding(tok.text, tok.lemma_, tok.tag_)
        factor = 1 / log(depth)
        if not tok.is_stop:
            factor *= .2
        if tok.tag_ in vblist:
            if vsb is None:
                vsb = wemb
            else:
                vsb += (wemb * factor)
        elif tok.tag_ in nlist:
            if ns is None:
                ns = wemb
            else:
                ns += (wemb * factor)
    embedding = np.append(ns, vsb)
    return embedding
