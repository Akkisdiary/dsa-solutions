"""
912. Sort an Array
https://leetcode.com/problems/sort-an-array/description/
"""

from typing import List
from utils import TestRunner


class SolutionBubble:
    def sortArray(self, nums: List[int]) -> List[int]:
        k = len(nums) - 1
        while 0 <= k:
            for j in range(k):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            k -= 1
        return nums


class SolutionMerge:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.solve(0, len(nums) - 1, nums)

    def solve(self, start: int, end: int, nums) -> List[int]:
        if end - start <= 0:
            return nums
        mid = (start + end) // 2
        self.solve(start, mid, nums)
        self.solve(mid + 1, end, nums)
        return self.merge(start, mid, end, nums)

    def merge(self, start: int, mid: int, end: int, nums) -> List[int]:
        left, right = nums[start : mid + 1], nums[mid + 1 : end + 1]
        i, j, k = start, 0, 0
        while j < len(left) and k < len(right):
            if left[j] < right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1
        return nums


cases = [
    {"input": {"nums": [5, 2, 3, 1]}, "expected": [1, 2, 3, 5]},
    {"input": {"nums": [5, 1, 1, 2, 0, 0]}, "expected": [0, 0, 1, 1, 2, 5]},
    {
        "input": {"nums": [5, 1, 1, 2, 0, 0, 10]},
        "expected": [0, 0, 1, 1, 2, 5, 10],
    },
]


if __name__ == "__main__":
    TestRunner(SolutionBubble().sortArray).test(cases)
    TestRunner(SolutionMerge().sortArray).test(cases)
