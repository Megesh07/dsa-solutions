"""
Problem: Linked List Cycle
Difficulty: Easy
Link: https://leetcode.com/problems/linked-list-cycle/

Given the head of a linked list, determine if the linked list has a cycle.

Example:
    Input:  3 -> 2 -> 0 -> -4 (tail connects to node at index 1)
    Output: True

Approach: Floyd's Cycle Detection (Tortoise and Hare) — O(n) time, O(1) space
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def make_cycle(values: list[int], pos: int) -> ListNode | None:
    """Helper: create a linked list with a cycle at given position."""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


if __name__ == "__main__":
    print(has_cycle(make_cycle([3, 2, 0, -4], 1)))  # True
    print(has_cycle(make_cycle([1, 2], 0)))          # True
    print(has_cycle(make_cycle([1], -1)))            # False
