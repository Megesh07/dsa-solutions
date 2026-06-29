"""
Problem: Encode and Decode Strings
Difficulty: Medium
Link: https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a single string
and decode it back to the original list.

Example:
    Input: ["lint", "code", "love", "you"]
    Encoded: "4#lint4#code4#love3#you"
    Output: ["lint", "code", "love", "you"]

Approach: Length-prefixed encoding — O(n) encode, O(n) decode
"""


def encode(strs: list[str]) -> str:
    """Encode list of strings using 'length#string' format."""
    result = ""
    for s in strs:
        result += f"{len(s)}#{s}"
    return result


def decode(s: str) -> list[str]:
    """Decode encoded string back to list of strings."""
    result = []
    i = 0

    while i < len(s):
        # Find the delimiter '#'
        j = i
        while s[j] != "#":
            j += 1

        length = int(s[i:j])
        result.append(s[j + 1: j + 1 + length])
        i = j + 1 + length

    return result


if __name__ == "__main__":
    words = ["lint", "code", "love", "you"]
    encoded = encode(words)
    print(f"Encoded: {encoded}")                # 4#lint4#code4#love3#you
    print(f"Decoded: {decode(encoded)}")         # ['lint', 'code', 'love', 'you']

    edge = ["", "hello", ""]
    print(decode(encode(edge)))                  # ['', 'hello', '']
