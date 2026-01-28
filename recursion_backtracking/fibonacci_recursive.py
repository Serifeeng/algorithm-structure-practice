def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using recursion.

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

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == "__main__":
    number = 10
    print(fibonacci_recursive(number))

