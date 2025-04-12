"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""

from utils import TestRunner


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            # '(': ')',
            # '[': ']',
            # '{': '}',
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif mapping.get(c) == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(c)
        return len(stack) == 0


cases = [
    {"input": {"s": "()"}, "expected": True},
    {"input": {"s": "()[]{}"}, "expected": True},
    {"input": {"s": "(]"}, "expected": False},
    {"input": {"s": "([])"}, "expected": True},
    {"input": {"s": "(){}}{"}, "expected": False},
]

if __name__ == "__main__":
    TestRunner(Solution().isValid).test(cases)
