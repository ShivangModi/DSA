# Implement the graph data structure with the following functions:
# •	Find the degree/indegree/outdegree of the given node
# •	Findout DFS tree with respect to given source node and calculate the length of largest path
# •	Findout BFS tree with respect to given source node and calculate the length of largest path
# •	Findout the connected components/strongly connected components of the given undirected graph/directed graph
# •	Findout the shortest path (i.e., the path with minimum path cost) between two nodes 
# •	Findout the longest path (i.e., the path with maximum path cost) between two nodes 
# •	Check whether given graph is simple graph

# Undirected Graph
class UndirectedGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        for i in range(self.v):
            self.graph.append([0]*self.v)
    
    def addEdge(self, u, v, w=1):
        self.graph[u][v] = self.graph[v][u] = w
    
    def removeEdge(self, u, v):
        if self.graph[u][v] == 0:
            print(f"No edge between {u} and {v}")
            return
        self.graph[u][v] = self.graph[v][u] = 0

    def printGraph(self):
        print("Adjacency Matrix: ")
        for row in self.graph:
            for col in row:
                print(col, end=" ")
            print()

    def dfs(self, u, visited=None):
        if visited is None:
            print(f'\nDFS for startind node {u}:-', end=" ")
            visited = [False]*self.v
        visited[u] = True

        print(u, end=" ")
        for adj in range(self.v):
            if self.graph[u][adj]==1 and (not visited[adj]):
                self.dfs(adj, visited)

    def bfs(self, u):
        visited = [False]*self.v
        print(f'\nBFS for startind node {u}:-', end=" ")
        
        q = [u]
        visited[u] = True
        while q:
            vis = q[0]
            print(vis, end=" ")
            q.pop(0)

            for adj in range(self.v):
                if self.graph[vis][adj]==1 and (not visited[adj]):
                    q.append(adj)
                    visited[adj] = True
    
    def degree(self, u):
        print(f'\nDegree of {u}:- {self.graph[u].count(1)}')
    
    def connectedComponent(self):
        visited = [False]*self.v
        i = 1
        print("Following are connected component:")
        for u in range(self.v):
            if visited[u] == False:
                print(f"Component {i}:-", end=" ")
                self.dfs(u, visited)
                print()
                i += 1


# Directed Graph
class DirectedGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        for i in range(self.v):
            self.graph.append([0]*self.v)
    
    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = -1
    
    def removeEdge(self, u, v):
        if self.graph[u][v] == 0:
            print(f"No edge between {u} and {v}")
            return
        self.graph[u][v] = 0

    def printGraph(self):
        print("Adjacency Matrix: ")
        for row in self.graph:
            for col in row:
                print(col, end=" ")
            print()
    
    def dfs(self, u, visited=None):
        if visited is None:
            print(f'\nDFS for startind node {u}:-', end=" ")
            visited = [False]*self.v
        visited[u] = True

        print(u, end=" ")
        for adj in range(self.v):
            if self.graph[u][adj]==1 and (not visited[adj]):
                self.dfs(adj, visited)

    def bfs(self, u):
        visited = [False]*self.v
        print(f'\nBFS for startind node {u}:-', end=" ")
        
        q = [u]
        visited[u] = True
        while q:
            vis = q[0]
            print(vis, end=" ")
            q.pop(0)

            for adj in range(self.v):
                if self.graph[vis][adj]==1 and (not visited[adj]):
                    q.append(adj)
                    visited[adj] = True

    def indeg(self, u):
        print(f'\nIndegree of {u}:- {self.graph[u].count(-1)}')
    
    def outdeg(self, u):
        print(f'\nOutdegree of {u}:- {self.graph[u].count(1)}')
    
    def stronglyConnectedComponent(self):
        pass


if __name__ == "__main__":
    graph = UndirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    # graph.dfs(2)
    # graph.bfs(2)
    # for i in range(5):
    #     graph.degree(i)
    # graph.connectedComponent()

    graph = DirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    # graph.dfs(1)
    # graph.bfs(1)
    # for i in range(5):
    #     graph.indeg(i)
    #     graph.outdeg(i)