def two_pointers(arr, target):
    """
    Finds two numbers in a sorted list that add up to the target value
    using the two pointers technique.

    Parameters:
    arr (list): Sorted list of integers
    target (int): Target sum

    Returns:
    tuple: Indices of the two elements if found, otherwise (-1, -1)
    """

    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return -1, -1


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 6, 8, 9]
    target_value = 10

    index1, index2 = two_pointers(numbers, target_value)

    if index1 != -1:
        print(f"Elements found at indices {index1} and {index2}")
        print(f"Values: {numbers[index1]} + {numbers[index2]} = {target_value}")
    else:
        print("No valid pair found")
