def fibonacci_memoization(n, memo=None):
    """
    Calculates the nth Fibonacci number using memoization.

    Parameters:
    n (int): Non-negative integer
    memo (dict): Dictionary to store previously calculated values

    Returns:
    int: nth Fibonacci number
    """

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    number = 10
    print(fibonacci_memoization(number))

