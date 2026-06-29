"""
Problem: Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return True if t is an anagram of s.

Example:
    Input: s = "anagram", t = "nagaram"
    Output: True

Approach: Character Count / Sorting — O(n) time, O(1) space
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


# Alternative: Without Counter
def is_anagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # True
    print(is_anagram("rat", "car"))          # False
    print(is_anagram("a", "a"))              # True
