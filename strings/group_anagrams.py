"""
Problem: Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Approach: Hash Map with sorted string as key — O(n * k log k) time, O(n * k) space
         where n = number of strings, k = max string length
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the characters to form the canonical key
        key = tuple(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


# Alternative: Use character count tuple as key (O(n*k) total)
def group_anagrams_v2(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        anagram_map[tuple(count)].append(word)

    return list(anagram_map.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(group_anagrams([""]))   # [['']]
    print(group_anagrams(["a"]))  # [['a']]
