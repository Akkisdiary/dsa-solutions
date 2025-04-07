"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/
"""
from utils import TestRunner


class SolutionBrute:
    def canPartition(self, nums) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        def find(i, target):
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False

            if find(i + 1, target - nums[i]):
                return True
            return find(i + 1, target)

        return find(0, totalSum // 2)


class SolutionBetter:
    def canPartition(self, nums) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        memo = {}

        def find(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == 0:
                return True
            if target < 0 or i == len(nums):
                return False

            inc = find(i + 1, target - nums[i])
            memo[(i, target)] = inc
            if inc:
                return True
            exc = find(i + 1, target)
            memo[(i, target)] = exc
            return exc

        return find(0, totalSum // 2)


cases = [
    {
        "input": {
            "nums": [1, 5, 11, 5],
        },
        "expected": True,
    },
    {
        "input": {
            "nums": [1, 2, 3, 5],
        },
        "expected": False,
    },
    {
        "input": {
            "nums": [
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,100,100,100,100,100,100,100,100,100,100,
                100,100,100,99,97
            ],
        },
        "expected": False,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().canPartition).test(cases)
