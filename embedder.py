import spacy
from math import log
import numpy as np

vblist = ['VB', 'VBD', 'VBG', 'VBP', 'VBN', 'VBZ', 'RB', 'RBR', 'RBS', 'RP', 'WDT', 'WRB']
nlist = ['CD', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'PRP']
PNlist = ['NNP', 'NNPS']
embeddings = {}
embeddinglength = 300


def initEmbeddings():
    filename = "glove.840B.300d/glove.840B.300d-char.txt"
    infile = open(filename, "r")
    for line in infile:
        if len(line) > 0:
            line = line[0:len(line)-1]
            embedding = line.split(' ')
            char = embedding[0]
            embedding = embedding[1:]
            embeddings[char] = embedding


# add whatever else we need
# returns numpy array of embedding
# note that spacy has a
def getWordEmbedding(token):
    if token.has_vector:
        return token.vector
    elif len(embeddings) > 0:
        vector = [0.0] * embeddinglength
        for char in token.text:
            for i in range(0, embeddinglength):
                vector[i] += float(embeddings[char][i])
        for i in range(0, embeddinglength):
            vector[i] /= len(token.text)
        return np.array(vector)
    return defaultVector()


def defaultVector():
    return np.array([1.0] * embeddinglength)


# sentence is a unicode string.
# enlp is a instance of spacy which has been loaded with
# an appropriate model. if in doubt, spacy.load('en') should be provided
def getSentenceEmbedding(sentence, enlp):
    doc = enlp(sentence.strip())
    sentence = list(doc.sents)[0]
    vsb = None  # defaultVector()
    ns = None  # defaultVector()
    queue = [sentence.root, None]
    depth = 2
    while len(queue) > 1:
        if queue[0] is None:
            depth += 1
            queue.pop(0)
            queue.append(None)
            continue
        for child in queue[0].children:
            queue.append(child)
        tok = queue.pop(0)
        wemb = getWordEmbedding(tok)
        factor = 1 / log(depth)
        if not tok.is_stop and tok.tag_ not in PNlist:
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
    # endloop
    if ns is None:
        ns = defaultVector()
    if vsb is None:
        vsb = defaultVector()
    embedding = np.append(ns, vsb)
    return embedding
