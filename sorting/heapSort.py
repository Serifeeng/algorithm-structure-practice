def heapify(arr, n, i):
    """
    Converts a subtree into a max heap.

    Parameters:
    arr (list): List to be heapified
    n (int): Size of the heap
    i (int): Index of the root element
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sorts a list using the Heap Sort algorithm.

    Parameters:
    arr (list): List of elements to be sorted

    Returns:
    list: Sorted list
    """

    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

numbers = [12, 11, 13, 5, 6, 7]
print(heap_sort(numbers))

