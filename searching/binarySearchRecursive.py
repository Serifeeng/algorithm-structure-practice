def binary_search_recursive(arr, target, left, right):
    """
    Performs recursive binary search on a sorted list.

    Parameters:
    arr (list): Sorted list of elements
    target: Element to search for
    left (int): Left index
    right (int): Right index

    Returns:
    int: Index of target if found, otherwise -1
    """

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]
    target_value = 7

    result = binary_search_recursive(numbers, target_value, 0, len(numbers) - 1)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
