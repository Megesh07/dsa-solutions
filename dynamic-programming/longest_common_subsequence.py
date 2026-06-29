"""
Problem: Longest Common Subsequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

Example:
    Input: text1 = "abcde", text2 = "ace"
    Output: 3  (common subsequence "ace")

Approach: 2D DP — O(m * n) time, O(m * n) space
          Optimized: O(min(m, n)) space using two rows
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # dp[i][j] = LCS of text1[:i] and text2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_space_optimized(text1: str, text2: str) -> int:
    """O(min(m, n)) space optimized version."""
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    prev = [0] * (len(text2) + 1)
    curr = [0] * (len(text2) + 1)

    for c1 in text1:
        for j, c2 in enumerate(text2, 1):
            if c1 == c2:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (len(text2) + 1)

    return prev[len(text2)]


if __name__ == "__main__":
    print(longest_common_subsequence("abcde", "ace"))   # 3
    print(longest_common_subsequence("abc", "abc"))     # 3
    print(longest_common_subsequence("abc", "def"))     # 0
    print(lcs_space_optimized("abcde", "ace"))           # 3
