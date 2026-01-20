def sliding_window_max_sum(arr, k):
    """
    Finds the maximum sum of any subarray of size k
    using the sliding window technique.

    Parameters:
    arr (list): List of integers
    k (int): Size of the sliding window

    Returns:
    int: Maximum sum of a subarray of size k
    """

    if k > len(arr) or k <= 0:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


if __name__ == "__main__":
    numbers = [2, 1, 5, 1, 3, 2]
    window_size = 3

    result = sliding_window_max_sum(numbers, window_size)

    print(f"Maximum sum of subarray of size {window_size}: {result}")
