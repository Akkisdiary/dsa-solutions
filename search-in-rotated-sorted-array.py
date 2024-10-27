"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


class SolutionOptimal:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if target == nums[mid]:
                return mid
            if nums[i] > nums[j]:
                if nums[i] <= nums[mid]:
                    if nums[i] <= target < nums[mid]:
                        j = mid - 1
                    else:
                        i = mid + 1
                else:
                    if nums[mid] <= target <= nums[j]:
                        i = mid + 1
                    else:
                        j = mid - 1
            elif target > nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return -1


cases = [
    {
        "input": {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
        },
        "expected": 4,
    },
    {
        "input": {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
        },
        "expected": -1,
    },
    {
        "input": {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 6,
        },
        "expected": 2,
    },
    {
        "input": {
            "nums": [6, 7, 0, 1, 2, 4, 5],
            "target": 0,
        },
        "expected": 2,
    },
    {
        "input": {
            "nums": [6, 7, 10, 11, 2, 4, 5],
            "target": 11,
        },
        "expected": 3,
    },
    {
        "input": {
            "nums": [6, 7, 10, 11, 12, 4, 5],
            "target": 12,
        },
        "expected": 4,
    },
    {
        "input": {
            "nums": [0, 1, 2, 4, 5, 6, 7],
            "target": 2,
        },
        "expected": 2,
    },
    {
        "input": {
            "nums": [1],
            "target": 0,
        },
        "expected": -1,
    },
    {
        "input": {
            "nums": [3, 5, 1],
            "target": 3,
        },
        "expected": 0,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().search).test(cases)
