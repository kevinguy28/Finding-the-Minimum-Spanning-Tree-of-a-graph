# Graphs will be input as an list of edges. Each edge will be a tuple of the form (u,v,w)
# Where u and v represent the endpoints of an edge, and w represents the cost of that edge
# The function will also take as input n, the number of vertices in the graph
# The graph is undirected(you can travel from u to v or from v to u)
# Your function should output a list of edges from the original graph which form the minumum spanning tree

def minimum_spanning_tree(graph, n):
    traversedNodes = []
    traversedPaths = []
    graph = sortGraphByWeight(graph)
    totalWeight = graph[0][2]
    traversedNodes = addToTraversedNodes(graph[0], traversedNodes)
    traversedPaths.append(graph[0])
    return(findMinSpanTree(graph, n, traversedNodes, traversedPaths, totalWeight))


def findMinSpanTree(graph, n, traversedNodes, traversedPaths, totalWeight):
    if(n == len(traversedNodes)):
        return(traversedPaths)
    else:
        minWeightNode = None
        for i in range(len(traversedNodes)):
            for a in range(len(graph)):
                if(traversedNodes[i] == graph[a][0] or graph[a][1]):
                    if(graph[a] not in traversedPaths):
                        if(minWeightNode == None):
                            if((graph[a][0] in traversedNodes and graph[a][1] not in traversedNodes) or (graph[a][0] not in traversedNodes and graph[a][1] in traversedNodes)):
                                minWeightNode = graph[a]
                        else:
                            if((graph[a][0] in traversedNodes and graph[a][1] not in traversedNodes) or (graph[a][0] not in traversedNodes and graph[a][1] in traversedNodes)):
                                if(minWeightNode[2] > graph[a][2]):
                                    minWeightNode = graph[a]
        traversedNodes = addToTraversedNodes(minWeightNode, traversedNodes)
        traversedPaths.append(minWeightNode)
        totalWeight += minWeightNode[2]
        return(findMinSpanTree(graph, n, traversedNodes, traversedPaths, totalWeight))


# Sorts the nodes by ascending weights
def sortGraphByWeight(graph):
    graphHolder = 0
    for i in range(len(graph)-1, 0, -1):
        for a in range(i):
            if(graph[a][2] > graph[a+1][2]):
                graphHolder = graph[a]
                graph[a] = graph[a+1]
                graph[a+1] = graphHolder
    return(graph)

def addToTraversedNodes(theTuple, traversedNodes):
    for i in range(2):
        if(theTuple[i] not in traversedNodes):
            traversedNodes.append(theTuple[i])
    return(traversedNodes)

def print_graph(graph):
    k = 0
    for e in graph:
        k += e[2]
    print("Minimum Spanning Tree")
    print("---------------------")
    print("Weight:\t" + str(k))
    print("Edges:")
    print(graph)
    print("#####################\n\n")


g1 = [
    (0,1,2),
    (0,2,2),
    (1,2,1)
]

g2 = [
    (0,1,4),
    (0,2,3),
    (0,3,2),
    (0,4,7),
    (1,3,3),
    (2,3,1),
]

g3 = [
    (0,1,4),
    (0,2,3),
    (0,5,7),
    (2,3,4),
    (1,3,2),
    (2,4,7),
    (4,5,4),
    (5,9,1),
    (8,9,3),
    (5,8,2),
    (1,7,10),
    (5,6,5),
    (6,7,2),
    (7,8,1),
]

mst1 = minimum_spanning_tree(g1, 3)
print_graph(mst1) # Expeted Weight: 3

mst2 = minimum_spanning_tree(g2, 5)
print_graph(mst2) # Expeted Weight: 13

mst3 = minimum_spanning_tree(g3, 10)
print_graph(mst3) # Expeted Weight: 26
