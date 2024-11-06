#!/usr/bin/python3
from sys import argv

def is_safe(board, row, col, N):
    # Check if no queen is placed in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, N, solutions):
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N, solutions)
            board[row] = -1  # Backtrack

def main():
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the board (-1 indicates no queen placed)
    board = [-1] * N
    solutions = []

    # Find the solutions using backtracking
    solve_nqueens(board, 0, N, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
