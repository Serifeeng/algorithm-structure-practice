
def longest_common_subsequence(text1, text2):
    """
    Finds the length of the longest common subsequence between two strings.

    Parameters:
    text1 (str): First string
    text2 (str): Second string

    Returns:
    int: Length of the longest common subsequence
    """

    m = len(text1)
    n = len(text2)

    # DP table where dp[i][j] is the LCS length of text1[:i] and text2[:j]
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"

    print(longest_common_subsequence(text1, text2))
