"""
Problem: Remove Nth Node From End of List
Difficulty: Medium
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end and return the head.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
    Output: 1 -> 2 -> 3 -> 5

Approach: Two Pointers with gap of n — O(n) time, O(1) space (single pass)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked, linked_to_list


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0)
    dummy.next = head
    left = dummy
    right = head

    # Advance right pointer by n steps
    for _ in range(n):
        right = right.next

    # Move both until right reaches end
    while right:
        left = left.next
        right = right.next

    # Remove the nth node from end
    left.next = left.next.next

    return dummy.next


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4, 5])
    print(linked_to_list(remove_nth_from_end(head, 2)))  # [1, 2, 3, 5]

    head2 = list_to_linked([1])
    print(linked_to_list(remove_nth_from_end(head2, 1))) # []

    head3 = list_to_linked([1, 2])
    print(linked_to_list(remove_nth_from_end(head3, 1))) # [1]
