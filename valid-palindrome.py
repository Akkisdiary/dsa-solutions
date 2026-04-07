"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
"""

from utils import TestRunner


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip("<>?:\"{},./;'[]")
        i = 0
        j = len(s) - 1
        while i <= j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


cases = [
    {"input": {"s": "A man, a plan, a canal: Panama"}, "expected": True},
    {"input": {"s": "race a car"}, "expected": False},
    {"input": {"s": " "}, "expected": True},
    {"input": {"s": "Was it a car or a cat I saw?"}, "expected": True},
    {"input": {"s": "tab a cat"}, "expected": False},
]

if __name__ == "__main__":
    TestRunner(Solution().isPalindrome).test(cases)
