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
    numbers= [64,25,12,22,11]
    print("Original list:",numbers)

    sorted_numbers=selection_sort(numbers)
    print("Sorted list:", sorted_numbers)


# Selection Sort is used to sort a list of elements.
# The algorithm repeatedly finds the minimum element from the unsorted part
# and places it at the correct position.
# The list does not need to be sorted beforehand.
# It is an in-place algorithm and does not require extra memory.
# It is not a stable algorithm; the order of equal elements may change.
# The time complexity is O(n^2) in all cases.
# The space complexity is O(1).
# The logic is very simple, making it easy to learn and understand.
# It performs poorly on large datasets.
# It is generally not preferred in real-world or production applications.

