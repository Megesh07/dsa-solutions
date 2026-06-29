"""
Problem: Word Ladder
Difficulty: Hard
Link: https://leetcode.com/problems/word-ladder/

Given beginWord, endWord and wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord where each step changes exactly
one letter and every intermediate word must be in wordList.

Example:
    Input: beginWord = "hit", endWord = "cog"
            wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5  (hit -> hot -> dot -> dog -> cog)

Approach: BFS — O(n * m^2) time where n = wordList size, m = word length
"""

from collections import deque, defaultdict


def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    # Build pattern map: *ot -> [hot, dot, lot]
    pattern_map = defaultdict(list)
    all_words = [begin_word] + list(word_set)
    for word in all_words:
        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            pattern_map[pattern].append(word)

    visited = {begin_word}
    queue = deque([(begin_word, 1)])

    while queue:
        word, steps = queue.popleft()

        for i in range(len(word)):
            pattern = word[:i] + "*" + word[i + 1:]
            for neighbor in pattern_map[pattern]:
                if neighbor == end_word:
                    return steps + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

    return 0


if __name__ == "__main__":
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
    print(ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))          # 0
    print(ladder_length("a", "c", ["a", "b", "c"]))                                  # 2
