def coin_change(coins, amount):
    """
    Finds the minimum number of coins needed to make up a given amount.

    Parameters:
    coins (list): List of coin denominations
    amount (int): Target amount

    Returns:
    int: Minimum number of coins, or -1 if not possible
    """

    # Initialize DP array with a value greater than any possible solution
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # Build the DP table
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(coin_change(coins, amount))

