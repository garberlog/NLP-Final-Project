from graph_tool.all import *
import spacy
import embedder
import numpy as np


def similarity(arr1, arr2):
    num = 0.0
    for i in range(0, len(arr1)):
        num += arr1.item(i) * arr2.item(i)
    return num / (np.linalg.norm(arr1) * np.linalg.norm(arr2))


def createindex():
    index = []
    nlp = spacy.load('en_vectors_web_lg')
    for i in range(0, 30):
        index.append([str(i), embedder.makeSentenceEmbeddings(unicode(str(i), "UTF-8"), nlp)])
    return index


# makes a graph for textrank
# index: a list of nodes with the form index[ID] = [text, vector]
# similarity: a function such that similarity(index[a][1], index[b][1]) 
# returns the similaity unichrbetween sentences a and b
# Returns a graph G with edge property "weight" for weights
def makegraph(index):
    g = Graph(directed=False)
    weight = g.new_edge_property("float")
    i = 0
    while i < len(index):
        g.add_vertex()
        j = 0
        while j < i:
            e = g.add_edge(g.vertex(i), g.vertex(j))
            weight[e] = similarity(index[i][1], index[j][1])
            j += 1
        i += 1
    g.edge_properties["weight"] = weight
    return g


# accepts a graph of format returned by makeGraph
# returns a property map of the pagerank pg.
# can be used via pg[g.vertex(i)] == pagerank of vertex with ID = i
def pagerank(g):
    pgr = graph_tool.centrality.pagerank(g, damping=.85, weight=g.edge_properties["weight"], epsilon=1e-6,
                                         max_iter=None)
    return pgr


# index: a list of nodes with the form index[ID] = [text, vector]
# similarity: a function such that similarity(index[a][1], index[b][1]) 
# modifies index such that it appends the pagerank to the index.
def textrank(index):
    g = makegraph(index)
    pgr = pagerank(g)
    printresults(index, pgr)


def printresults(index, pgr):
    percentage = 35
    pageArr = pgr.get_array()
    threshold = sorted(pageArr, reverse=True)[(len(pageArr) * percentage / 100)]
    for i in range(0, len(index)):
        if pageArr[i] >= threshold:
            print(index[i][0])


# Debugging
index = createindex()
# call parse on input
# call do coref with parsed input as argument
textrank(index)
