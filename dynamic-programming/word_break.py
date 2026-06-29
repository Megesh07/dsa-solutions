"""
Problem: Word Break
Difficulty: Medium
Link: https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return True if s can be
segmented into a space-separated sequence of one or more dictionary words.

Example:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: True

Approach: DP — O(n^2 * m) time where n = len(s), m = avg word length
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    word_set = set(word_dict)
    n = len(s)

    # dp[i] = True if s[:i] can be segmented using wordDict
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always segmentable

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))           # True
    print(word_break("applepenapple", ["apple", "pen"]))      # True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
