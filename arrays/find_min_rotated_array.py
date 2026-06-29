"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given a sorted rotated array of unique elements, return the minimum element.
Must run in O(log n) time.

Example:
    Input: nums = [3, 4, 5, 1, 2]
    Output: 1

Approach: Binary Search — O(log n) time, O(1) space
"""


def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    return nums[left]


if __name__ == "__main__":
    print(find_min([3, 4, 5, 1, 2]))        # 1
    print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(find_min([11, 13, 15, 17]))        # 11
