#!/usr/bin/python3
'''Shows possible arrangements of N-queens on a chess board'''
import sys

def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens(board, col):
    if col == len(board):
        for row in range(len(board)):
            solution = []
            for col in range(len(board)):
                if board[row][col] == 1:
                    solution.append([row, col])
            print(solution)
        return True

    found_solution = False
    for row in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            found_solution = solve_n_queens(board, col + 1) or found_solution
            board[row][col] = 0

    return found_solution

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0)
