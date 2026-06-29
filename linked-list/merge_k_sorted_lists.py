"""
Problem: Merge K Sorted Lists
Difficulty: Hard
Link: https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked lists, each linked list is sorted in ascending order.
Merge all the linked lists into one sorted linked list and return it.

Example:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: 1->1->2->3->4->4->5->6

Approach: Min-Heap (Priority Queue) — O(n log k) time, O(k) space
"""

import heapq
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from node import ListNode, list_to_linked, linked_to_list


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    # Min-heap: (value, index, node) — index breaks ties
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next

        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


if __name__ == "__main__":
    lists = [
        list_to_linked([1, 4, 5]),
        list_to_linked([1, 3, 4]),
        list_to_linked([2, 6]),
    ]
    print(linked_to_list(merge_k_lists(lists)))  # [1,1,2,3,4,4,5,6]
    print(linked_to_list(merge_k_lists([])))     # []
