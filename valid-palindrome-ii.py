"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/description/
"""

from utils import TestRunner


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l + 1, r) or self.isPalindrome(
                    s, l, r - 1
                )
            l += 1
            r -= 1
        return True

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


cases = [
    {"input": {"s": "aba"}, "expected": True},
    {"input": {"s": "abca"}, "expected": True},
    {"input": {"s": "abc"}, "expected": False},
    {"input": {"s": "deeeeee"}, "expected": True},
]

if __name__ == "__main__":
    TestRunner(Solution().validPalindrome).test(cases)
