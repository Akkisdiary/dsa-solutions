"""
Sort a Stack
https://www.naukri.com/code360/problems/sort-a-stack_985275
"""

from utils import TestRunner


class SolutionBrute:
    def sortStack(self, stack):
        return list(stack).sort()


cases = [
    {"input": {"stack": [4, 1, 2]}, "expected": [4, 2, 1]},
    {"input": {"stack": [5, -2, 9, -7, 3]}, "expected": [9, 5, 3, -2, -7]},
    {
        "input": {"stack": [-3, 14, 18, -5, 30]},
        "expected": [30, 18, 14, -3, -5],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().sortStack).test(cases)
