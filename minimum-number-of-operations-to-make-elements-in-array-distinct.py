"""
3396. Minimum Number of Operations to Make Elements in Array Distinct
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/?envType=daily-question&envId=2025-04-08
"""
from typing import List
from utils import TestRunner


class SolutionBrute:
    # time: O(n*n) ; space: O(n)
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(0, len(nums), 3):
            new = nums[i:]
            if len(set(new)) == len(new):
                return ops
            ops += 1
        return ops


class SolutionBetter:
    # time: O(n + 3n) ; space: O(n)
    def minimumOperations(self, nums: List[int]) -> int:
        memo = {}
        for n in nums:
            memo[n] = memo.get(n, 0) + 1
        ops = 0
        for i in range(0, len(nums), 3):
            if len(memo) == len(nums) - i:
                return ops
            for j in range(i, min(len(nums), i + 3)):
                if nums[j] in memo:
                    freq = memo.pop(nums[j], 0) - 1
                    if freq > 0:
                        memo[nums[j]] = freq
            ops += 1
        return ops


class SolutionOptimal:
    # time: O(n) ; space: O(n)
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0


cases = [
    {"input": {"nums": [1, 2, 3, 4, 2, 3, 3, 5, 7]}, "expected": 2},
    {"input": {"nums": [4, 5, 6, 4, 4]}, "expected": 2},
    {"input": {"nums": [6, 7, 8, 9]}, "expected": 0},
    {"input": {"nums": [5, 5]}, "expected": 1},
    {"input": {"nums": [3, 7, 7, 3]}, "expected": 1},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().minimumOperations).test(cases)
    TestRunner(SolutionBetter().minimumOperations).test(cases)
    TestRunner(SolutionOptimal().minimumOperations).test(cases)
