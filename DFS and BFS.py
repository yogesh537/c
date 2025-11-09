# ----- Breadth First Search -----
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # For BFS
queue = []

def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS Traversal:")
bfs('A')

# ----- Depth First Search -----
visited_dfs = set()

def dfs(node):
    if node not in visited_dfs:
        print(node, end=" ")
        visited_dfs.add(node)
        for neighbour in graph[node]:
            dfs(neighbour)

print("\nDFS Traversal:")
dfs('A')
