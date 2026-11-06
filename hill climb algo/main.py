import random

N = 8

def heuristic(board):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j]:
                conflicts += 1

            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing():
    board = [random.randint(0, N-1) for _ in range(N)]

    while True:
        current_h = heuristic(board)

        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        for col in range(N):
            for row in range(N):
                if row != board[col]:
                    neighbor = board[:]
                    neighbor[col] = row

                    h = heuristic(neighbor)

                    if h < best_h:
                        best_h = h
                        best_board = neighbor

        if best_h >= current_h:
            return None

        board = best_board


solution = hill_climbing()

if solution:
    print("Solution:", solution)

    for row in range(N):
        for col in range(N):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("Local minimum reached. No solution found.")