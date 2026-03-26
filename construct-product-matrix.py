# 2906. Construct Product Matrix
# https://leetcode.com/problems/construct-product-matrix/?envType=daily-question&envId=2026-03-24

from typing import List
from utils import TestRunner


class SolutionBrute:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        p = [[1 for _ in range(m)] for _ in range(n)]

        totalProd = 1
        for i in range(n):
            for j in range(m):
                totalProd *= grid[i][j]

        for i in range(n):
            for j in range(m):
                prod = totalProd // grid[i][j]
                p[i][j] = prod % 12345

        return p


cases = [
    {"input": {"grid": [[1, 2], [3, 4]]}, "expected": [[24, 12], [8, 6]]},
    {"input": {"grid": [[12345], [2], [1]]}, "expected": [[2], [0], [0]]},
    {
        "input": {"grid": [[451605717, 288123249], [125076807, 619416616]]},
        "expected": [[10743, 8049], [6018, 11751]],
    },
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().constructProductMatrix).test(cases)
