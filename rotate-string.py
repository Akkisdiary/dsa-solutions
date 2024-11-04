"""
796. Rotate String
https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2024-11-03
"""

from utils import TestRunner


class SolutionBrute:
    def rotateString(self, s: str, goal: str) -> bool:
        shifts = 0
        while shifts < len(s):
            s = s[1:] + s[:1]
            if goal == s:
                return True
            shifts += 1
        return False


class SolutionBetter:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        return goal in s + s


cases = [
    {
        "input": {
            "s": "abcde",
            "goal": "cdeab",
        },
        "expected": True,
    },
    {
        "input": {
            "s": "abcde",
            "goal": "abced",
        },
        "expected": False,
    },
    {
        "input": {
            "s": "abcdeabcde",
            "goal": "abcedabcde",
        },
        "expected": False,
    },
    {
        "input": {
            "s": "abcdeabcde",
            "goal": "eabcdeabcd",
        },
        "expected": True,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().rotateString).test(cases)
    TestRunner(SolutionBetter().rotateString).test(cases)
