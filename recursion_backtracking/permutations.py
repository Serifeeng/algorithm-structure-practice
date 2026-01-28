
def permutations(arr):
    """
    Generates all permutations of the given list.

    Parameters:
    arr (list): Input list

    Returns:
    list: List of all permutations
    """

    result = []
    used = [False] * len(arr)
    current = []

    def backtrack():
        if len(current) == len(arr):
            result.append(current.copy())
            return

        for i in range(len(arr)):
            if not used[i]:
                used[i] = True
                current.append(arr[i])
                backtrack()
                current.pop()
                used[i] = False

    backtrack()
    return result


if __name__ == "__main__":
    data = [1, 2, 3]
    print(permutations(data))
