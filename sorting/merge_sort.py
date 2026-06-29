"""
Algorithm: Merge Sort
Complexity: O(n log n) time, O(n) space
Stability: Stable (preserves relative order of equal elements)

Merge Sort uses divide-and-conquer:
1. Divide the array in half
2. Recursively sort each half
3. Merge the two sorted halves

It is the preferred algorithm when stability matters or when sorting linked lists.
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Returns a new sorted list."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr: list[int], left: int = 0, right: int = None) -> None:
    """In-place merge sort variant."""
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)
    _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr: list[int], left: int, mid: int, right: int) -> None:
    temp = arr[left:right + 1]
    i, j = 0, mid - left + 1
    k = left

    while i <= mid - left and j <= right - left:
        if temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1
        k += 1

    while i <= mid - left:
        arr[k] = temp[i]
        i += 1
        k += 1

    while j <= right - left:
        arr[k] = temp[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr))  # [3, 9, 10, 27, 38, 43, 82]

    arr2 = [5, 2, 8, 1, 9, 3]
    merge_sort_inplace(arr2)
    print(arr2)  # [1, 2, 3, 5, 8, 9]
