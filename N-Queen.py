# ---------- N-Queen Problem (Dynamic Input Version) ----------

def print_board(board, N):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def is_safe(board, row, col, N):
    # Check left side of the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueen(board, col, N):
    # Base case: if all queens are placed
    if col >= N:
        print_board(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nqueen(board, col + 1, N) or res
            board[i][col] = 0  # backtrack

    return res


# ---------- Main Program ----------
N = int(input("Enter the number of queens (N): "))

board = [[0] * N for _ in range(N)]

print(f"\nAll possible solutions for {N}-Queen problem:\n")
if not solve_nqueen(board, 0, N):
    print("No solution exists.")
