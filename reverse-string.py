"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
"""

from typing import List
from utils import TestRunner


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s


cases = [
    {"input": {"s": ["n", "e", "e", "t"]}, "expected": ["t", "e", "e", "n"]},
    {
        "input": {"s": ["h", "e", "l", "l", "o"]},
        "expected": ["o", "l", "l", "e", "h"],
    },
    {
        "input": {"s": ["H", "a", "n", "n", "a", "h"]},
        "expected": ["h", "a", "n", "n", "a", "H"],
    },
]

if __name__ == "__main__":
    TestRunner(Solution().reverseString).test(cases)
