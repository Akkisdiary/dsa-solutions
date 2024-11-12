"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/description/
"""

from typing import List
from collections import deque

from utils import TestRunner


class SolutionBrute:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for n in nums1:
            ans.append(self.find(n, nums2))
        return ans

    def find(self, num: int, nums2: List[int]):
        i = 0
        while i < len(nums2):
            if nums2[i] == num:
                break
            i += 1
        i += 1
        while i < len(nums2):
            if nums2[i] > num:
                return nums2[i]
            i += 1
        return -1


class SolutionBetter:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = deque()
        memo = {}

        for i in range(len(nums2) - 1, -1, -1):
            ng = -1
            while len(stack) > 0:
                top = stack.pop()
                if top > nums2[i]:
                    ng = top
                    stack.append(top)
                    break
            memo[nums2[i]] = ng
            stack.append(nums2[i])

        ans = []
        for i in range(len(nums1)):
            ans.append(memo.get(nums1[i]))
        return ans


cases = [
    {"input": {"nums1": [4, 1, 2], "nums2": [1, 3, 4, 2]}, "expected": [-1, 3, -1]},
    {"input": {"nums1": [2, 4], "nums2": [1, 2, 3, 4]}, "expected": [3, -1]},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().nextGreaterElement).test(cases)
    TestRunner(SolutionBetter().nextGreaterElement).test(cases)
