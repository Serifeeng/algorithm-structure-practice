def linear_search(arr, target):
    """
    Performs linear search on the given list.

    Parameters:
    arr (list): List of elements to search in
    target: Element to be searched

    Returns:
    int: Index of target if found, otherwise -1
    """

    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1


if __name__ == "__main__":
    numbers = [5, 3, 8, 4, 2]
    target_value = 4

    result = linear_search(numbers, target_value)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
