"""
Shared ListNode definition for all linked list problems.
Import this in other modules using: from linked_list.node import ListNode
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        values = []
        curr = self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return " -> ".join(values)


def list_to_linked(values: list[int]) -> ListNode | None:
    """Helper: Convert a Python list to a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def linked_to_list(head: ListNode | None) -> list[int]:
    """Helper: Convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
