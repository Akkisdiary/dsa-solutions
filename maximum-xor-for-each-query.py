"""
1829. Maximum XOR for Each Query
https://leetcode.com/problems/maximum-xor-for-each-query
"""

from typing import List

from utils import TestRunner


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        xor = 0
        for n in nums:
            xor = xor ^ n
        i = len(nums) - 1
        target = (2**maximumBit) - 1
        while i >= 0:
            ans.append(xor ^ target)
            xor = xor ^ nums[i]
            i -= 1
        return ans


cases = [
    {
        "input": {
            "nums": [0,1,1,3],
            "maximumBit": 2
        },
        "expected": [0,3,2,3],
    },
    {
        "input": {
            "nums": [2,3,4,7],
            "maximumBit": 3
        },
        "expected": [5,2,6,5],
    },
    {
        "input": {
            "nums": [0,1,2,2,5,7],
            "maximumBit": 3
        },
        "expected": [4,3,6,4,6,7],
    }
]

if __name__ == "__main__":
    TestRunner(Solution().getMaximumXor).test(cases)
