# ---------- Dynamic Alpha-Beta Pruning Example ----------

def alpha_beta(depth, node, isMaximizing, values, alpha, beta, maxDepth):
    # Base case: if at leaf node
    if depth == maxDepth:
        return values[node]
    
    if isMaximizing:
        best = -9999
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, False, values, alpha, beta, maxDepth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (MAX node)")
                break
        return best
    else:
        best = 9999
        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i, True, values, alpha, beta, maxDepth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned at depth {depth} (MIN node)")
                break
        return best


# ---------- Take dynamic input ----------
print("Alpha–Beta Pruning Simulation")
maxDepth = int(input("Enter depth of game tree (e.g., 3): "))

total_nodes = 2 ** maxDepth
values = []

print(f"Enter {total_nodes} leaf node values (space separated):")
values = list(map(int, input().split()))

if len(values) != total_nodes:
    print("Error: Number of values must be exactly", total_nodes)
else:
    print("\nEvaluating game tree...")
    best_score = alpha_beta(0, 0, True, values, -9999, 9999, maxDepth)
    print("\nBest possible value for MAX player is:", best_score)
