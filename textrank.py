from graph_tool.all import *


def createindex():
    index = []
    for i in range(0, 30):
        index.append([str(i), random.random()])
    return index


# makes a graph for textrank
# index: a list of nodes with the form index[ID] = [text, vector]
# similarity: a function such that similarity(index[a][1], index[b][1]) 
# returns the similaity between sentences a and b
# Returns a graph G with edge property "weight" for weights
def makegraph(index, similarity):
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
# returns: 
def textrank(index, similarity):
    g = makegraph(index, similarity)
    pgr = pagerank(g)
    printresults(index, pgr, g)


def printresults(index, pgr, g):
    pageArr = pgr.get_array()
    numAllowed = int(len(pageArr) * .35)
    results = []
    for i in range(0, len(pageArr)):
        val = pageArr[i]
        sen = index[i][0]
        for j in range(0, numAllowed):
            if j >= len(results):
                results.append([sen, val])
                break
            elif val > results[j][1]:
                tempSen = sen
                tempVal = val
                sen = results[j][0]
                val = results[j][1]
                results[j][0] = tempSen
                results[j][1] = tempVal
    for i in range(0, len(results)):
        print(results[i][0])

# Debugging
# import random
# index = createindex()
# similarity = lambda x, y: 1 - abs(x - y)
# textrank(index, similarity)
