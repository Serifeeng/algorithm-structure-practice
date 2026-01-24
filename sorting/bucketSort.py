def bucket_sort(arr):
    """
    Sorts a list of floating-point numbers using the Bucket Sort algorithm.

    Parameters:
    arr (list): List of numbers between 0 and 1

    Returns:
    list: Sorted list
    """

    if len(arr) == 0:
        return arr

    # Create empty buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Put elements into different buckets
    for num in arr:
        index = int(bucket_count * num)
        if index == bucket_count:  # Edge case for num == 1
            index -= 1
        buckets[index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate all buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


numbers = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(numbers))
