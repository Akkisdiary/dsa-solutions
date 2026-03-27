# 2946. Matrix Similarity After Cyclic Shifts
# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description/?envType=daily-question&envId=2026-03-27

from typing import List
from utils import TestRunner


class SolutionBrute:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n, m = len(mat), len(mat[0])
        k = k % m
        if k == m:
            return True

        for r in range(n):
            if r % 2 == 0:
                i = m - 1
                j = i - k
                while i >= 0:
                    if mat[r][i] != mat[r][j]:
                        return False
                    i -= 1
                    j -= 1
                    if j < 0:
                        j = m - 1
            else:
                i = 0
                j = i + k
                while i < m:
                    if mat[r][i] != mat[r][j]:
                        return False
                    i += 1
                    j += 1
                    if j >= m:
                        j = 0

        return True


cases = [
    {
        "input": {"mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "k": 4},
        "expected": False,
    },
    {
        "input": {"mat": [[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], "k": 2},
        "expected": True,
    },
    {"input": {"mat": [[2, 2], [2, 2]], "k": 3}, "expected": True},
    {
        "input": {
            "mat": [
                [3, 3, 3, 3, 3, 3],
                [5, 3, 5, 3, 5, 3],
                [2, 5, 2, 5, 2, 5],
                [8, 8, 8, 8, 8, 8],
                [3, 8, 3, 8, 3, 8],
                [5, 3, 5, 3, 5, 3],
                [1, 8, 1, 8, 1, 8],
                [8, 9, 8, 9, 8, 9],
                [2, 8, 2, 8, 2, 8],
            ],
            "k": 4,
        },
        "expected": True,
    },
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().areSimilar).test(cases)
