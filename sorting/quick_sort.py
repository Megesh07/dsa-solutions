"""
Algorithm: Quick Sort
Complexity: O(n log n) average, O(n^2) worst case, O(log n) space
Stability: NOT stable

Quick Sort uses divide-and-conquer with a pivot element:
1. Choose a pivot
2. Partition: elements < pivot go left, elements > pivot go right
3. Recursively sort left and right partitions

It is generally faster than merge sort in practice due to better cache performance.
Using random pivot avoids worst-case O(n^2) on sorted input.
"""

import random


def quick_sort(arr: list[int], low: int = 0, high: int = None) -> None:
    """In-place quicksort."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    """Lomuto partition scheme with random pivot."""
    # Random pivot to avoid worst case on sorted arrays
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]

    pivot = arr[high]
    i = low - 1  # Index of last element smaller than pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_functional(arr: list[int]) -> list[int]:
    """Functional (non-in-place) version for clarity."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort_functional(left) + middle + quick_sort_functional(right)


if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    quick_sort(arr)
    print(arr)  # [11, 12, 22, 25, 64]

    arr2 = [3, 6, 8, 10, 1, 2, 1]
    print(quick_sort_functional(arr2))  # [1, 1, 2, 3, 6, 8, 10]

    # Already sorted (would be worst case without random pivot)
    arr3 = list(range(100, 0, -1))
    quick_sort(arr3)
    print(arr3[:5], "...", arr3[-5:])  # [1, 2, 3, 4, 5] ... [96, 97, 98, 99, 100]
