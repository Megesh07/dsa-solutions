"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example:
    Input: s = "abcabcbb"
    Output: 3  (substring "abc")

Approach: Sliding Window — O(n) time, O(min(n, m)) space where m = charset size
"""


def length_of_longest_substring(s: str) -> int:
    char_index = {}
    max_len = 0
    left = 0

    for right, char in enumerate(s):
        # If char was seen and is within our current window, shrink from left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # 3
    print(length_of_longest_substring("bbbbb"))     # 1
    print(length_of_longest_substring("pwwkew"))    # 3
    print(length_of_longest_substring(""))          # 0
