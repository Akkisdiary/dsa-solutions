# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/description/

from collections import deque
from utils import TestRunner


class SolutionBrute:
    def orangesRotting(self, grid):
        time = 0
        while not self.isRotten(grid):
            print(grid)
            if not self.isPossible(grid):
                return -1
            self.elapse(grid)
            time += 1
        return time

    def elapse(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    for di, dj in directions:
                        if (
                            0 <= i + di < m
                            and 0 <= j + dj < n
                            and grid[i + di][j + dj] == 1
                        ):
                            grid[i + di][j + dj] = -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    grid[i][j] = 2

    def isRotten(self, grid):
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return False
        return True

    def isPossible(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                for di, dj in directions:
                    if (
                        0 <= i + di < m
                        and 0 <= j + dj < n
                        and grid[i + di][j + dj] == 2
                    ):
                        return True
        return False


class SolutionBetter:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh, time = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while len(q) > 0 and fresh > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    if (
                        0 <= i + di < m
                        and 0 <= j + dj < n
                        and grid[i + di][j + dj] == 1
                    ):
                        grid[i + di][j + dj] = 2
                        q.append((i + di, j + dj))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1


cases = [
    {"input": {"grid": [[2, 1, 1], [1, 1, 0], [0, 1, 1]]}, "expected": 4},
    {"input": {"grid": [[0, 2]]}, "expected": 0},
    {"input": {"grid": [[0, 2, 0], [0, 0, 0], [1, 1, 1]]}, "expected": -1},
    {"input": {"grid": [[0]]}, "expected": 0},
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().orangesRotting).test(cases)
