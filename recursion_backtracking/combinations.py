def combinations(arr, r):
    """
    Generates all possible combinations of length r from the given list.

    Parameters:
    arr (list): Input list
    r (int): Length of each combination

    Returns:
    list: List of combinations
    """

    result = []
    current = []

    def backtrack(start):
        if len(current) == r:
            result.append(current.copy())
            return

        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result


if __name__ == "__main__":
    data = [1, 2, 3, 4]
    r = 2
    print(combinations(data, r))

