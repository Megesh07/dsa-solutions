"""
Problem: Minimum Window Substring
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.

Example:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

Approach: Sliding Window with two frequency maps — O(n) time, O(k) space
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)       # Characters needed and their counts
    have = {}               # Characters we currently have in window
    formed = 0              # Number of unique chars satisfied
    required = len(need)    # Number of unique chars we need

    left = 0
    min_len = float("inf")
    result = ""

    for right in range(len(s)):
        char = s[right]
        have[char] = have.get(char, 0) + 1

        # Check if current char satisfies a requirement
        if char in need and have[char] == need[char]:
            formed += 1

        # Try to contract the window while it's valid
        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                result = s[left:right + 1]

            left_char = s[left]
            have[left_char] -= 1
            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1
            left += 1

    return result


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))  # "BANC"
    print(min_window("a", "a"))                # "a"
    print(min_window("a", "aa"))               # ""
