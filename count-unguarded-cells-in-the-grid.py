"""
2257. Count Unguarded Cells in the Grid
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        # 0 = free, 1 = wall, 2 = guard, 3 = guarded

        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2

        def mark(row, col):
            for r in range(row + 1, m):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3
            for r in range(row - 1, -1, -1):
                if grid[r][col] in (1, 2):
                    break
                grid[r][col] = 3
            for c in range(col + 1, n):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3
            for c in range(col - 1, -1, -1):
                if grid[row][c] in (1, 2):
                    break
                grid[row][c] = 3

        for r, c in guards:
            mark(r, c)

        res = 0
        for row in grid:
            for n in row:
                if n == 0:
                    res += 1
        return res


cases = [
    {
        "input": {
            "m": 4,
            "n": 6,
            "guards": [[0, 0], [1, 1], [2, 3]],
            "walls": [[0, 1], [2, 2], [1, 4]],
        },
        "expected": 7,
    },
    {
        "input": {
            "m": 4,
            "n": 6,
            "guards": [[0, 0], [1, 1], [2, 3], [2, 5]],
            "walls": [[0, 1], [2, 2], [1, 4]],
        },
        "expected": 4,
    },
    {
        "input": {
            "m": 3,
            "n": 3,
            "guards": [[1, 1]],
            "walls": [[0, 1], [1, 0], [2, 1], [1, 2]],
        },
        "expected": 4,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().countUnguarded).test(cases)
