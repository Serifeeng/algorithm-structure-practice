def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.

    Parameters:
    arr (list): List of elements to be sorted

    Returns:
    list: Sorted list
    """

    # Base case: a list of zero or one elements is already sorted
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Divide the list into left and right halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """

    merged = []
    i = j = 0

    # Compare elements from both lists and merge them in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", numbers)

    sorted_numbers = merge_sort(numbers)
    print("Sorted list:", sorted_numbers)
