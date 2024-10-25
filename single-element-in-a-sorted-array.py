"""
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/description/
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
        return nums[len(nums) - 1]


class SolutionBetter:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def find(i: int, j: int):
            mid = (i + j) // 2
            if i > j:
                return

            if any(
                (
                    mid == 0 and nums[mid] != nums[mid + 1],
                    mid == len(nums) - 1 and nums[mid] != nums[mid - 1],
                )
            ):
                return nums[mid]

            if all((nums[mid] != nums[mid - 1], nums[mid] != nums[mid + 1])):
                return nums[mid]

            left = find(i, mid - 1)
            if left is not None:
                return left
            return find(mid + 1, j)

        return find(0, len(nums) - 1)


class SolutionOptimal:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        i = 1
        j = n - 2
        while i <= j:
            mid = (i + j) // 2
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            if any((
                mid % 2 == 0 and nums[mid] != nums[mid + 1],
                mid % 2 == 1 and nums[mid] != nums[mid - 1],
            )):
                j = mid - 1
            else:
                i = mid + 1

        return -1


cases = [
    {
        "input": {
            "nums": [1, 1, 2, 3, 3, 4, 4, 8, 8],
        },
        "expected": 2,
    },
    {
        "input": {
            "nums": [3, 3, 7, 7, 10, 11, 11],
        },
        "expected": 10,
    },
    {
        "input": {
            "nums": [3, 7, 7],
        },
        "expected": 3,
    },
    {
        "input": {
            "nums": [3, 3, 7],
        },
        "expected": 7,
    },
    {
        "input": {
            "nums": [3, 3, 4, 4, 7],
        },
        "expected": 7,
    },
    {
        "input": {
            "nums": [3],
        },
        "expected": 3,
    },
    {
        "input": {
            "nums": [7, 7, 10, 11, 11, 12, 12],
        },
        "expected": 10,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().singleNonDuplicate).test(cases)
