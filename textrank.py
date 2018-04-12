from graph_tool.all import *

#makes a graph for textrank
# index: a list of nodes with the form index[ID] = [text, vector]
# similarity: a function such that similarity(index[a][1], index[b][1]) 
# returns the similaity between sentences a and b
# Returns a graph G with edge property "weight" for weights
def makeGraph(index, similarity):
	g = Graph(directed=False)
	weight = g.new_edge_property("float")
	i = 0
	while i < len(index):
		g.add_vertex()
		j = 0
		while j < i:
			e = g.add_edge(g.vertex(i), g.vertex(j))
			weight[e] = similarity(index[i][1], index[j][1])
			j +=1
		i+=1
	g.edge_properties["weight"] = weight
	return g

#accepts a graph of format returned by makeGraph
#returns a property map of the pagerank pg. 
# can be used via pg[g.vertex(i)] == pagerank of vertex with ID = i
def pageRank(g):
	pgr = graph_tool.centrality.pagerank(g, damping=.85, weight=g.edge_properties["weight"], epsilon= 1e-6, max_iter=None)
	return pgr

# index: a list of nodes with the form index[ID] = [text, vector]
# similarity: a function such that similarity(index[a][1], index[b][1]) 
# returns: 
def textrank(index, similarity):
	g = makeGraph(index, similarity)
	pgr = pageRank(g)
	
#### Debugging
#import random
#index = []
#for i in range(0, 30):
#	index.append([str(i), random.random()])
#similarity = lambda x, y: 1 - abs(x - y)
#g = makeGraph(index, similarity)
#print(pageRank(g))
