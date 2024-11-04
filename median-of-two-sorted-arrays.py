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


class SolutionBetter:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        n = n1 + n2
        half = (n + 1) // 2
        i = 0
        j = n1
        while i <= j:
            mid1 = (i + j) // 2
            mid2 = half - mid1

            l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1-1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2-1]

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                j = mid1 - 1
            else:
                i = mid1 + 1
        return -1


cases = [
    {
        "input": {"nums1": [1, 3], "nums2": [2]},
        "expected": 2.0,
    },
    {
        "input": {
            "nums1": [2, 3, 6, 15],
            "nums2": [1, 3, 4, 7, 10, 12],
        },
        "expected": 5,
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
    TestRunner(SolutionBetter().findMedianSortedArrays).test(cases)
