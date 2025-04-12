"""
Median in a row-wise sorted Matrix
https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def median(self, matrix: List[List[int]], R: int, C: int) -> int:
        elements = []
        for i in range(R):
            for j in range(C):
                elements.append(matrix[i][j])
        elements.sort()
        return elements[R * C // 2]


class SolutionOptimal:
    def median(self, matrix: List[List[int]], R: int, C: int) -> int:
        low = float("inf")
        high = float("-inf")

        for i in range(R):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][C - 1])

        def countSmallerThan(elem):
            def upperBound(row, num):
                i = 0
                j = C - 1
                while i <= j:
                    mid = (i + j) // 2
                    # print(f"{i=}, {j=}, {mid=}, {num=}")
                    if row[mid] < num:
                        i = mid + 1
                    else:
                        j = mid - 1
                return j

            count = 0
            for i in range(R):
                count += upperBound(matrix[i], elem) + 1
            return count

        req = ((R * C) // 2) + 1
        while low <= high:
            mid = (low + high) // 2
            if countSmallerThan(mid) < req:
                low = mid + 1
            else:
                high = mid - 1

        return high


cases = [
    {
        "input": {"matrix": [[1, 3, 5], [2, 6, 9], [3, 6, 9]], "R": 3, "C": 3},
        "expected": 5,
    },
    {
        "input": {"matrix": [[1, 3, 6], [2, 5, 9], [3, 6, 9]], "R": 3, "C": 3},
        "expected": 5,
    },
    {"input": {"matrix": [[1], [2], [3]], "R": 3, "C": 1}, "expected": 2},
    {"input": {"matrix": [[1, 2, 3]], "R": 1, "C": 3}, "expected": 2},
    {"input": {"matrix": [[1]], "R": 1, "C": 1}, "expected": 1},
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().median).test(cases)
