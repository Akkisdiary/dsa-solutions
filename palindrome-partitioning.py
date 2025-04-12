# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/

from utils import TestRunner


class Solution:
    def partition(self, s):
        parts = []
        part = []

        def solve(index):
            if index == len(s):
                parts.append(part[:])
                return
            for i in range(index, len(s)):
                if self.is_palindrome(s, index, i):
                    part.append(s[index : i + 1])
                    solve(i + 1)
                    part.pop(-1)

        solve(0)
        return parts

    def is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


cases = [
    {"input": {"s": "aab"}, "expected": [["a", "a", "b"], ["aa", "b"]]},
    {"input": {"s": "a"}, "expected": [["a"]]},
    {
        "input": {"s": "abcba"},
        "expected": [["a", "b", "c", "b", "a"], ["a", "bcb", "a"], ["abcba"]],
    },
]

if __name__ == "__main__":
    TestRunner(Solution().partition).test(cases, sorted)
