def climbing_stairs(n):
    """
    Calculates the number of distinct ways to climb to the top.

    You can climb either 1 or 2 steps at a time.

    Parameters:
    n (int): Number of steps

    Returns:
    int: Number of distinct ways
    """

    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    prev2 = 1  # ways to reach step 0
    prev1 = 1  # ways to reach step 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    steps = 5
    print(climbing_stairs(steps))

