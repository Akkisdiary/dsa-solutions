# 27. Remove Element
# https://leetcode.com/problems/remove-element/

from typing import List
from utils import TestRunner


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1
        return i


cases = [
    {"input": {"nums": [3, 2, 2, 3], "val": 3}, "expected": 2},
    {"input": {"nums": [1], "val": 1}, "expected": 0},
    {"input": {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2}, "expected": 5},
]

if __name__ == "__main__":
    TestRunner(Solution().removeElement).test(cases)
