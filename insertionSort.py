def insertion_sort(arr):
    """
    Sorts a list using the Insertion Sort algorithm.

    Parameters:
    arr (list): List of elements to be sorted

    Returns:
    list: Sorted list
    """

    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place key at its correct position
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    numbers = [8, 3, 5, 2, 9, 1]
    print("Original list:", numbers)

    sorted_numbers = insertion_sort(numbers)
    print("Sorted list:", sorted_numbers)
