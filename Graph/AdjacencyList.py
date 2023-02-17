# Implement the graph data structure with the following functions:
# •	Find the degree/indegree/outdegree of the given node
# •	Findout DFS tree with respect to given source node and calculate the length of largest path
# •	Findout BFS tree with respect to given source node and calculate the length of largest path
# •	Findout the connected components/strongly connected components of the given undirected graph/directed graph
# •	Findout the shortest path (i.e., the path with minimum path cost) between two nodes 
# •	Findout the longest path (i.e., the path with maximum path cost) between two nodes 
# •	Check whether given graph is simple graph

class UndirectedGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        for i in range(self.v):
            self.graph.append(list())
    
    def addEdge(self, u, v):
        # Adding node v to the source node u
        self.graph[u].append(v)

        # Adding node u to the source node v
        self.graph[v].append(u)

    def printGraph(self):
        for i in range(self.v):
            print(f"Adjacency list of vertex {i}: {i}", end=" -> ")
            for adj in self.graph[i]:
                print(f"{adj}", end=" -> ")
            print(None)
    
    def dfs(self, u, visited=None):
        if visited is None:
            print(f'\nDFS for startind node {u}:-', end=" ")
            visited = [False]*self.v
        visited[u] = True

        print(u, end=" ")
        for adj in self.graph[u]:
            if not visited[adj]:
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

            for adj in self.graph[vis]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True

    def degree(self, u):
        print(f'\nDegree of {u}:- {len(self.graph[u])}')
    
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


class DirectedGraph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        for i in range(self.v):
            self.graph.append(list())
    
    def addEdge(self, u, v):
        # Adding node v to the source node u
        self.graph[u].append(v)

    def printGraph(self):
        for i in range(self.v):
            print(f"Adjacency list of vertex {i}: {i}", end=" -> ")
            for adj in self.graph[i]:
                print(f"{adj}", end=" -> ")
            print(None)
    
    def dfs(self, u, visited=None):
        if visited is None:
            print(f'\nDFS for startind node {u}:-', end=" ")
            visited = [False]*self.v
        visited[u] = True

        print(u, end=" ")
        for adj in self.graph[u]:
            if not visited[adj]:
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

            for adj in self.graph[vis]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True

    def indeg(self, u):
        cnt = 0
        for i in range(self.v):
            if u in self.graph[i]:
                cnt += 1
        print(f'\nDegree of {u}:- {cnt}')
    
    def outdeg(self, u):
        print(f'\nDegree of {u}:- {len(self.graph[u])}')
    
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
    graph.connectedComponent()
    # graph.printGraph()
    # graph.dfs(2)
    # graph.bfs(2)
    # for i in range(5):
    #     graph.degree(i)

    graph = DirectedGraph(5)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    # graph.printGraph()
    # graph.dfs(1)
    # graph.bfs(1)
    # for i in range(5):
    #     graph.indeg(i)
    #     graph.outdeg(i)