# 3740. Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/?envType=daily-question&envId=2026-04-10

from typing import List
from utils import TestRunner
from collections import defaultdict

class SolutionBrute:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1
        mini = n + 1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        m = abs(i - j) + abs(j - k) + abs(k - i)
                        mini = min(mini, m)
        if mini != n + 1:
            return mini
        return -1


class SolutionBetter:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2


cases = [
    {"input": {"nums": [1, 2, 1, 1, 3]}, "expected": 6},
    {"input": {"nums": [1, 1, 2, 3, 2, 1, 2]}, "expected": 8},
    {"input": {"nums": [1, 1, 1, 3, 2, 2, 2]}, "expected": 4},
    {"input": {"nums": [1, 2, 1, 3, 2, 2, 2]}, "expected": 4},
    {"input": {"nums": [1, 4, 1, 3, 2, 2, 4, 2]}, "expected": 6},
    {"input": {"nums": [1, 4, 1, 1, 3, 2, 4, 2]}, "expected": 6},
    {"input": {"nums": [1, 2, 3, 4, 5, 6, 7, 8]}, "expected": -1},
    {"input": {"nums": [1]}, "expected": -1},
    {"input": {"nums": [5, 3, 5, 5, 5]}, "expected": 4},
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().minimumDistance).test(cases)
    TestRunner(SolutionBetter().minimumDistance).test(cases)
