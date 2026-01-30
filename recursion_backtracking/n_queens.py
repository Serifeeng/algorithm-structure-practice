
def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.
    Parameters:
    n (int): Size of the chessboard (n x n)
    Returns:
    list: All possible solutions, each solution is a list where
          index represents row and value represents column
    """

    solutions = []
    board =[-1]*n  # board[row] = column

    def is_safe(row, col):
        for prev_row in range(row):
            # Same column or same diagonal
            if (
                board[prev_row] == col or
                abs(board[prev_row] - col) == abs(prev_row - row)
            ):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            if is_safe(row, col):
                board[row]= col
                backtrack(row+1)
                board[row]= -1

    backtrack(0)
    return solutions


def print_solutions(solutions):
    """
    Prints the N-Queens solutions in a readable board format.
    """
    for idx, solution in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        for col in solution:
            row = ["." for _ in range(len(solution))]
            row[col] = "Q"
            print(" ".join(row))
        print()


if __name__ == "__main__":
    n =4
    solutions = solve_n_queens(n)

    print(f"Total solutions for {n}-Queens:", len(solutions))
    print_solutions(solutions)
