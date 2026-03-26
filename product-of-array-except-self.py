# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List
from utils import TestRunner


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1, 2, 3, 4]
        [24, 12, 4, 1]
        [24, 12, 24]
        n = len(nums)
        p = [0] * n

        suffix = 1
        for i in range(n - 1, -1, -1):
            p[i] = suffix
            suffix *= nums[i]

        prefix = 1
        for i in range(n):
            p[i] *= prefix
            prefix *= nums[i]

        return p


cases = [
    {"input": {"nums": [1, 2, 3, 4]}, "expected": [24, 12, 8, 6]},
    {"input": {"nums": [-1, 1, 0, -3, 3]}, "expected": [0, 0, 9, 0, 0]},
]

if __name__ == "__main__":
    TestRunner(Solution().productExceptSelf).test(cases, sorted)
