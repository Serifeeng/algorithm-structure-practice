import bisect

def longest_increasing_subsequence(nums):
    """
    Returns the length of the Longest Increasing Subsequence (LIS).
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    sub = []

    for num in nums:
        idx = bisect.bisect_left(sub, num)
        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num

    return len(sub)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(longest_increasing_subsequence(nums))  # 4

