def knapsack_01(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Parameters:
    weights (list): Weights of the items
    values (list): Values of the items
    capacity (int): Maximum capacity of the knapsack

    Returns:
    int: Maximum value that can be obtained
    """

    n = len(weights)

    # DP table where dp[i][w] is the maximum value using first i items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print(knapsack_01(weights, values, capacity))

