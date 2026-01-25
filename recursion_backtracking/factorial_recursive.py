def factorial_recursive(n):
    """
    Calculates the factorial of a number using recursion.

    Parameters:
    n (int): Non-negative integer

    Returns:
    int: Factorial of n
    """

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    number = 5
    print(factorial_recursive(number))

