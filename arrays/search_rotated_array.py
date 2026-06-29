"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Given a sorted rotated array and a target, return the index of target or -1 if not found.
Must run in O(log n) time.

Example:
    Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    Output: 4

Approach: Modified Binary Search — O(log n) time, O(1) space
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(search([1], 0))                      # -1
