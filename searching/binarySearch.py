
def binary_search(arr, target):

    """
    Performs binary search on a sorted list.
    arr (list): Sorted list of elements
    target: Element to search for
    int: Index of target if found, otherwise -1
    """

    left=0
    right=len(arr)-1

    while left<=right:
        mid= (right+left)//2

        # If target is found at mid
        if arr[mid]==target:
            return mid
        
        # If target is greater, ignore left half
        if arr[mid]< target:
            left=mid+1

        # If target is smaller, ignore right half
        else:
            right= mid-1

    # Target not found
    return -1


if __name__=="__main__":
    numbers=[1, 3, 5, 7, 9, 11, 13, 15]   
    target=15

    result=binary_search(numbers,target) 
    if result!=-1:
        print(f"target value {target} found at index {result+1}")
    else:
        print(f"target value {target} not found in the list")


# Works only on sorted arrays
# Uses an iterative (loop-based) approach
# Repeatedly divides the search range into half
# Time Complexity: O(log n)
# Space Complexity: O(1) since no recursion is used
# More memory-efficient than recursive version
# Commonly preferred in production systems
