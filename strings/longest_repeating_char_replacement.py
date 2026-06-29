"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character and change it to
any uppercase English letter at most k times. Return the length of the longest substring
containing the same letter you can get after performing the operations.

Example:
    Input: s = "AABABBA", k = 1
    Output: 4

Approach: Sliding Window — O(n) time, O(1) space (26-char alphabet)
"""


def character_replacement(s: str, k: int) -> int:
    count = {}
    max_count = 0  # count of the most frequent char in the window
    max_len = 0
    left = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        max_count = max(max_count, count[s[right]])

        # Window size - max_count = characters we need to replace
        # If replacements needed > k, shrink window
        window_size = right - left + 1
        if window_size - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(character_replacement("ABAB", 2))    # 4
    print(character_replacement("AABABBA", 1)) # 4
