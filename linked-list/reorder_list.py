"""
Problem: Reorder List
Difficulty: Medium
Link: https://leetcode.com/problems/reorder-list/

Given list L0 -> L1 -> ... -> Ln, reorder it to:
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 1 -> 5 -> 2 -> 4 -> 3

Approach: Find middle + reverse second half + merge — O(n) time, O(1) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked, linked_to_list


def reorder_list(head: ListNode | None) -> None:
    """Modifies the list in-place."""
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second = slow.next
    slow.next = None  # Cut the list in half
    prev = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    second = prev  # Head of reversed second half

    # Step 3: Merge the two halves
    first = head
    while second:
        tmp1 = first.next
        tmp2 = second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4])
    reorder_list(head)
    print(linked_to_list(head))  # [1, 4, 2, 3]

    head2 = list_to_linked([1, 2, 3, 4, 5])
    reorder_list(head2)
    print(linked_to_list(head2))  # [1, 5, 2, 4, 3]
