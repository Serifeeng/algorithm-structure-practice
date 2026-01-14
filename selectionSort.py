def selection_sort(arr):
    """
    Sorts a list using the Selection Sort algorithm.

    Parameters:
    arr (list): List of elements to be sorted

    Returns:
    list: Sorted list
    """

    n = len(arr)

    # Move the boundary of the unsorted subarray
    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    numbers = [64, 25, 12, 22, 11]
    print("Original list:", numbers)

    sorted_numbers = selection_sort(numbers)
    print("Sorted list:", sorted_numbers)
