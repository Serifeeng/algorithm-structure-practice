def fibonacci_dp(n):
    """
    Calculates the nth Fibonacci number using dynamic programming (bottom-up).

    Parameters:
    n (int): Non-negative integer

    Returns:
    int: nth Fibonacci number
    """

    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")

    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == "__main__":
    number = 10
    print(fibonacci_dp(number))

