import sys

def prim_mst(graph):
    V = len(graph)
    selected = [False] * V  # Track vertices included in MST
    keys = [sys.maxsize] * V  # Values to pick minimum weight edge
    parents = [-1] * V  # Array to store MST structure

    # Start from the first vertex
    keys[0] = 0

    for _ in range(V):
        # Pick the minimum key vertex not yet included in MST
        min_key = sys.maxsize
        u = -1
        for v in range(V):
            if not selected[v] and keys[v] < min_key:
                min_key = keys[v]
                u = v

        # Include vertex u in MST
        selected[u] = True

        # Update keys and parents of adjacent vertices of u
        for v in range(V):
            # graph[u][v] is weight of edge u-v
            if graph[u][v] > 0 and not selected[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parents[v] = u

    # Print the constructed MST
    print("Edge \tWeight")
    total_weight = 0
    for i in range(1, V):
        print(f"{parents[i]} - {i} \t {graph[i][parents[i]]}")
        total_weight += graph[i][parents[i]]
    print("Total weight of MST:", total_weight)

# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)

