# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/

from dsa.utils import TestRunner


class SolutionBrute:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


class SolutionOptimal:
    def twoSum(self, nums, target):
        memo = {}
        for i, n in enumerate(nums):
            if memo.get(target-n):
                return i, memo.get(target-n)
            memo[n] = i

        for i, n in enumerate(nums):
            if memo.get(target-n):
                return i, memo.get(target-n)
            memo[n] = i


test_cases = [
    {
        "input": {
            "nums": [2, 7, 11, 15],
            "target": 9
        },
        "expected": [0, 1]
    },
    {
        "input": {
            "nums": [3, 2, 4],
            "target": 6
        },
        "expected": [1, 2]
    },
    {
        "input": {
            "nums": [3, 3],
            "target": 6
        },
        "expected": [0, 1]
    },
    {
        "input": {
            "nums": [-5, 3, 5],
            "target": 0
        },
        "expected": [0, 2]
    },
    {
        "input": {
            "nums": [0, 1, -2],
            "target": -2
        },
        "expected": [0, 2]
    },
    {
        "input": {
            "nums": [0, 1, -2],
            "target": -1
        },
        "expected": [1, 2]
    },
    {
        "input": {
            "nums": [0, 1, -2, 84, 0, 28, 45],
            "target": 26
        },
        "expected": [2, 5]
    },
]
for case in test_cases:
    TestRunner(
        SolutionOptimal().twoSum,
    ).case(case).test(lambda x: list(sorted(x)))
