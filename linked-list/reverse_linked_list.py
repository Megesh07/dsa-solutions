"""
Problem: Reverse Linked List
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list and return the reversed list.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: 5 -> 4 -> 3 -> 2 -> 1

Approach: Iterative (two pointers) — O(n) time, O(1) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked, linked_to_list


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Save next
        curr.next = prev       # Reverse link
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

    return prev


# Recursive approach
def reverse_list_recursive(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    head = list_to_linked([1, 2, 3, 4, 5])
    print(linked_to_list(reverse_list(head)))   # [5, 4, 3, 2, 1]

    head2 = list_to_linked([1, 2])
    print(linked_to_list(reverse_list(head2)))  # [2, 1]
