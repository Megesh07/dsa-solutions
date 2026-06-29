"""
Problem: Valid Parentheses
Difficulty: Easy
Link: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

Example:
    Input: s = "()[]{}"
    Output: True

Approach: Stack — O(n) time, O(n) space
"""


def is_valid(s: str) -> bool:
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in matching:
            # It's a closing bracket
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
        else:
            # It's an opening bracket
            stack.append(char)

    return len(stack) == 0


if __name__ == "__main__":
    print(is_valid("()"))      # True
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))      # False
    print(is_valid("([)]"))    # False
    print(is_valid("{[]}"))    # True
