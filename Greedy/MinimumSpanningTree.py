# What is a Spanning Tree?
# - Given an undirected and connected graph G(V, E), a spanning tree of 
#   the graph G is a tree that spans G (that is, it includes every vertex 
#   of G) and is a subgraph of G (every edge in the tree belongs to G)

# What is a Minimum Spanning Tree?
# - The cost of the spanning tree is the sum of the weights of all the 
#   edges in the tree. There can be many spanning trees. Minimum spanning 
#   tree is the spanning tree where the cost is minimum among all the 
#   spanning trees. There also can be many minimum spanning trees.
# - Minimum spanning tree has direct application in the design of networks. 
#   It is used in algorithms approximating the travelling salesman problem, 
#   multi-terminal minimum cut problem and minimum-cost weighted perfect 
#   matching. Other practical applications are:
#       1. Cluster Analysis
#       2. Handwriting recognition
#       3. Image segmentation

# Algorithm:    Prim's, Kruskal's & Boruvka's algorithm
import sys


class UndirectedGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        for i in range(self.v):
            self.graph.append([0] * self.v)

    def addEdge(self, u, v, w=1):
        self.graph[u][v] = self.graph[v][u] = w


class MinimumSpanningTree:
    def __init__(self, graph):
        self.v = len(graph)
        self.graph = graph
        # removing the self loop
        for i in range(self.v):
            self.graph[i][i] = 0

    def __minKey(self, key, mstSet):
        # initialize min value
        min = sys.maxsize
        for v in range(self.v):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def __printPrimMST(self, parent):
        print("Prim's Algorithm")
        print("Edge \tWeight")
        for i in range(1, self.v):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
        print()

    def primMST(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.v
        parent = [None] * self.v  # Array to store constructed MST

        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.v

        parent[0] = -1  # First node is always the root of
        for cout in range(self.v):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.__minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.v):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if 0 < self.graph[u][v] < key[v] and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.__printPrimMST(parent)


if __name__ == "__main__":
    g = UndirectedGraph(5)
    g.addEdge(0, 1, 2)
    g.addEdge(0, 3, 6)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 8)
    g.addEdge(1, 4, 5)
    g.addEdge(2, 4, 7)
    g.addEdge(3, 4, 9)

    mst = MinimumSpanningTree(g.graph)
    mst.primMST()
