def counting_sort_for_radix(arr, exp):
    """
    A stable counting sort used as a subroutine for Radix Sort.

    Parameters:
    arr (list): List of non-negative integers
    exp (int): Current digit place (1, 10, 100, ...)

    Returns:
    None
    """

    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count array to store actual positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (stable sort)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy output to arr
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Sorts a list of non-negative integers using the Radix Sort algorithm.

    Parameters:
    arr (list): List of non-negative integers

    Returns:
    list: Sorted list
    """

    if len(arr) == 0:
        return arr

    max_value = max(arr)
    exp = 1

    # Sort numbers digit by digit
    while max_value // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

numbers = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(numbers))
