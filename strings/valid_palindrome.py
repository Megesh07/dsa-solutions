"""
Problem: Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters to lowercase and
removing all non-alphanumeric characters, it reads the same forward and backward.

Example:
    Input: s = "A man, a plan, a canal: Panama"
    Output: True

Approach: Two Pointers — O(n) time, O(1) space
"""


def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))                       # False
    print(is_palindrome(" "))                                # True
