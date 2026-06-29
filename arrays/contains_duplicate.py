"""
Problem: Contains Duplicate
Difficulty: Easy
Link: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears at least twice.

Example:
    Input: nums = [1, 2, 3, 1]
    Output: True

Approach: Hash Set — O(n) time, O(n) space
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))     # True
    print(contains_duplicate([1, 2, 3, 4]))     # False
    print(contains_duplicate([1, 1, 1, 3, 3]))  # True
