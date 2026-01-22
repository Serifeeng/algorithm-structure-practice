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

# Purpose: Find an element in a list by checking each element one by one from start to end
# No requirement for the list to be sorted
# Simple and effective for small datasets
# Logic is very straightforward: compare elements sequentially
# Time Complexity: O(n)
# Space Complexity: O(1)
# Slower than Binary Search, but works in all cases
# Commonly used for debugging and quick-check scenarios
