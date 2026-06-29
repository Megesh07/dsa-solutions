"""
Problem: LRU Cache
Difficulty: Medium
Link: https://leetcode.com/problems/lru-cache/

Design a data structure that follows the Least Recently Used (LRU) cache constraint.

Implement LRUCache class:
- LRUCache(int capacity): Initialize with positive capacity
- int get(int key): Return value if exists, else -1
- void put(int key, int value): Insert/update key. If capacity exceeded, evict LRU.

All operations must run in O(1) average time.

Approach: Doubly Linked List + Hash Map — O(1) get and put
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()  # Ordered by insertion/access time

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)   # cache: {1:1}
    lru.put(2, 2)   # cache: {1:1, 2:2}
    print(lru.get(1))   # 1, cache: {2:2, 1:1}
    lru.put(3, 3)       # evicts 2, cache: {1:1, 3:3}
    print(lru.get(2))   # -1 (not found)
    lru.put(4, 4)       # evicts 1, cache: {3:3, 4:4}
    print(lru.get(1))   # -1
    print(lru.get(3))   # 3
    print(lru.get(4))   # 4
