"""
2615. Sum of Distances
https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23
"""

from typing import List
from collections import defaultdict

from utils import TestRunner


class SolutionBrute:
    def distance(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    arr[i] += abs(i - j)
        return arr


class SolutionBetter:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        memo = defaultdict(list)
        arr = [0] * n
        for i in range(n):
            memo[nums[i]].append(i)
        for i in range(n):
            for j in memo[nums[i]]:
                if i != j:
                    arr[i] += abs(i - j)
        return arr


cases = [
    {"input": {"nums": [1, 3, 1, 1, 2]}, "expected": [5, 0, 3, 4, 0]},
    {"input": {"nums": [0, 5, 3]}, "expected": [0, 0, 0]},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().distance).test(cases)
    TestRunner(SolutionBetter().distance).test(cases)
