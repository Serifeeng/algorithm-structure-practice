
def counting_sort(arr):
    """
    Sorts a list of non-negative integers using the Counting Sort algorithm.

    Parameters:
    arr (list): List of non-negative integers

    Returns:
    list: Sorted list
    """

    if len(arr) == 0:
        return arr

    max_value = max(arr)

    # Create count array
    count = [0] * (max_value + 1)

    # Store the count of each element
    for num in arr:
        count[num] += 1

    # Build the sorted array
    sorted_arr = []
    for value in range(len(count)):
        sorted_arr.extend([value] * count[value])

    return sorted_arr

numbers = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(numbers))
