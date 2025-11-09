# ---------- Super Simple A* Algorithm ----------

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0, 'F': 0}

def astar(start, goal):
    open_list = [start]          # nodes to explore
    closed_list = []             # explored nodes
    g = {start: 0}               # cost from start
    parent = {start: None}       # track path

    while len(open_list) > 0:
        # Step 1: choose the node with smallest (cost + heuristic)
        best_node = open_list[0]
        best_value = g[best_node] + heuristic[best_node]
        for n in open_list:
            value = g[n] + heuristic[n]
            if value < best_value:
                best_value = value
                best_node = n

        current = best_node
        open_list.remove(current)
        closed_list.append(current)

        # Step 2: goal check
        if current == goal:
            path = []
            while current is not None:
                path.insert(0, current)
                current = parent[current]
            print("Shortest Path:", " → ".join(path))
            print("Total Cost:", g[goal])
            return

        # Step 3: check neighbors
        for neighbor in graph[current]:
            cost = g[current] + graph[current][neighbor]

            # if neighbor never visited
            if neighbor not in g:
                g[neighbor] = cost
                parent[neighbor] = current
                open_list.append(neighbor)

            # if found cheaper path
            elif cost < g[neighbor]:
                g[neighbor] = cost
                parent[neighbor] = current

            print("Visited:", neighbor, " | Cost so far =", cost)

    print("No path found!")

# Example run
astar('A', 'F')
