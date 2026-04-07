"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""

from re import L
from typing import List
from utils import TestRunner


class SolutionBrute:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        for i in range(len(height)):
            for j in range(i, len(height)):
                water = min(height[i], height[j]) * (j - i)
                maxi = max(maxi, water)
        return maxi


class SolutionBetter:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        maxi = 0
        while i < j:
            water = min(height[i], height[j]) * (j - i)
            maxi = max(maxi, water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxi


cases = [
    {"input": {"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, "expected": 49},
    {"input": {"height": [1, 1]}, "expected": 1},
    {"input": {"height": [2, 2, 2]}, "expected": 4},
    {"input": {"height": [1, 7, 2, 5, 4, 7, 3, 6]}, "expected": 36},
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().maxArea).test(cases)
