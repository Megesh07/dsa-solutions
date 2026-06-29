"""
Problem: Find The Duplicate Number
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-duplicate-number/

Given an array nums containing n+1 integers where each integer is in range [1, n],
find the one duplicate number. Must not modify the array. O(1) extra space.

Example:
    Input: nums = [1, 3, 4, 2, 2]
    Output: 2

Approach: Floyd's Cycle Detection on implicit linked list — O(n) time, O(1) space
         (nums[i] acts as the "next pointer" from index i)
"""


def find_duplicate(nums: list[int]) -> int:
    # Phase 1: Find the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the entrance to the cycle (= duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))  # 2
    print(find_duplicate([3, 1, 3, 4, 2]))  # 3
    print(find_duplicate([1, 1]))           # 1
