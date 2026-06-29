"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as one sorted list.

Example:
    Input:  l1 = 1->2->4, l2 = 1->3->4
    Output: 1->1->2->3->4->4

Approach: Iterative with dummy head — O(n + m) time, O(1) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked, linked_to_list


def merge_two_lists(
    l1: ListNode | None, l2: ListNode | None
) -> ListNode | None:
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Attach the remaining list
    curr.next = l1 if l1 else l2

    return dummy.next


if __name__ == "__main__":
    l1 = list_to_linked([1, 2, 4])
    l2 = list_to_linked([1, 3, 4])
    print(linked_to_list(merge_two_lists(l1, l2)))  # [1,1,2,3,4,4]

    print(linked_to_list(merge_two_lists(None, None)))  # []
