# 2530. Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description

import math
from utils import TestRunner


class SolutionBrute:
    def maxKelements(self, nums, k):
        score = i = 0
        while i < len(nums) and k > 0:
            nums.sort(reverse=True)
            score += nums[i]
            nums[i] = math.ceil(nums[i] / 3)
            k -= 1
        return score


class SolutionBetter:
    def maxKelements(self, nums, k):
        score = 0
        while k > 0:
            idx = 0
            maxi = 0
            for i in range(len(nums)):
                if nums[i] > maxi:
                    maxi = nums[i]
                    idx = i
            score += nums[idx]
            nums[idx] = math.ceil(nums[idx] / 3)
            k -= 1
        return score


cases = [
    {"input": {"nums": [10, 10, 10, 10, 10], "k": 5}, "expected": 50},
    {"input": {"nums": [1, 10, 3, 3, 3], "k": 3}, "expected": 17},
    {"input": {"nums": [10, 9, 8, 4, 3, 3, 2, 1], "k": 5}, "expected": 35},
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().maxKelements).test(cases)
