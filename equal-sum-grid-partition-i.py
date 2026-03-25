"""
3546. Equal Sum Grid Partition I
https://leetcode.com/problems/equal-sum-grid-partition-i/description/
"""

from utils import TestRunner


class SolutionBrute:
    def canPartitionGrid(self, grid) -> bool:
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            if self.subGridSum(0, i + 1, 0, c, grid) == self.subGridSum(
                i + 1, r, 0, c, grid
            ):
                return True
        for i in range(c):
            if self.subGridSum(0, r, 0, i + 1, grid) == self.subGridSum(
                0, r, i + 1, c, grid
            ):
                return True
        return False

    def subGridSum(self, r1, r2, c1, c2, grid):
        s = 0
        for i in range(r1, r2):
            for j in range(c1, c2):
                s += grid[i][j]
        return s


class SolutionBetter:
    def canPartitionGrid(self, grid) -> bool:
        return self.canPartitionGridByRow(
            grid
        ) or self.canPartitionGridByColumn(grid)

    def canPartitionGridByRow(self, grid) -> bool:
        r = len(grid)
        if r <= 1:
            return False
        t = 0
        b = r - 1
        st = sb = 0
        while t <= b:
            if st < sb:
                st += sum(grid[t])
                t += 1
            else:
                sb += sum(grid[b])
                b -= 1
        return st == sb

    def canPartitionGridByColumn(self, grid) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        if cols <= 1:
            return False
        l = 0
        r = cols - 1
        sl = sr = 0
        while l <= r:
            if sl < sr:
                for i in range(rows):
                    sl += grid[i][l]
                l += 1
            else:
                for i in range(rows):
                    sr += grid[i][r]
                r -= 1
            print(f"{sl=} {sr=}")
        return sl == sr


class SolutionOptimal:
    def canPartitionGrid(self, grid) -> bool:
        total = sum(map(sum, grid))
        if total % 2 != 0:
            return False
        target = total // 2
        s = 0
        for row in grid:
            s += sum(row)
            if s == target:
                return True
        s = 0
        for col in range(len(grid[0])):
            for i in range(len(grid)):
                s += grid[i][col]
                if s == target:
                    return True
        return False


cases = [
    {"input": {"grid": [[1, 4], [2, 3]]}, "expected": True},
    {"input": {"grid": [[1, 3], [2, 4]]}, "expected": False},
    {"input": {"grid": [[28443], [33959]]}, "expected": False},
    {"input": {"grid": [[42047], [57775], [99822]]}, "expected": True},
    {"input": {"grid": [[14742, 71685, 59237, 27190]]}, "expected": True},
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().canPartitionGrid).test(cases)
