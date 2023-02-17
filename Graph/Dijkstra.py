def constructPath(path, start, goal):
    temp = goal
    rev = temp
    while temp != start:
        rev += path[temp]
        temp = path[temp]
    print(rev[::-1])


def dijkstra(graph, start, goal):
    unvisited = {n: float('inf') for n in graph.keys()}
    unvisited[start] = 0

    visited = {}
    revPath = {}
    while unvisited:
        minNode = min(unvisited, key=unvisited.get)
        visited[minNode] = unvisited[minNode]

        if minNode == goal:
            break

        for neighbor in graph.get(minNode):
            if neighbor in visited:
                continue
            temp = unvisited[minNode] + graph[minNode][neighbor]
            if temp < unvisited[neighbor]:
                unvisited[neighbor] = temp
                revPath[neighbor] = minNode
        unvisited.pop(minNode)
    constructPath(revPath, start, goal)
    return visited[goal]


if __name__ == "__main__":
    graph = {
        'A': {'B': 2, 'C': 9, 'F': 4},
        'B': {'C': 6, 'E': 3, 'F': 2},
        'C': {'D': 1},
        'D': {'C': 2},
        'E': {'D': 5, 'C': 2},
        'F': {'E': 3}
    }
    start, goal = 'A', 'F'
    cost = dijkstra(graph, start, goal)
    print(f'The cost to reach from {start=} to {goal=}: {cost}')
