"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        temp = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < len(nums1):
            temp.append(nums1[i])
            i += 1
        while j < len(nums2):
            temp.append(nums2[j])
            j += 1
        n = len(temp)
        if n % 2 == 1:
            return temp[n // 2]
        else:
            return (temp[(n // 2) - 1] + temp[(n // 2)]) / 2


cases = [
    {
        "input": {"nums1": [1, 3], "nums2": [2]},
        "expected": 2.0,
    },
    {
        "input": {"nums1": [1, 2], "nums2": [3, 4]},
        "expected": 2.5,
    },
    {
        "input": {"nums1": [0, 1, 2, 4, 5, 6, 7], "nums2": [5, 6, 7]},
        "expected": 5.0,
    },
    {
        "input": {"nums1": [3, 3, 3, 4], "nums2": [1, 2, 2, 3]},
        "expected": 3,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().findMedianSortedArrays).test(cases)
