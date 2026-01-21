def quick_sort(arr):
    """
    Sorts a list using the Quick Sort algorithm.

    Parameters:
    arr (list): List of elements to be sorted

    Returns:
    list: Sorted list
    """

    # Base case: a list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (last element)
    pivot = arr[-1]

    left = []
    right = []

    # Partition the list
    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    # Recursively sort partitions and combine
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]
    print("Original list:", numbers)

    sorted_numbers = quick_sort(numbers)
    print("Sorted list:", sorted_numbers)
