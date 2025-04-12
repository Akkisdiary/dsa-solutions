# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/description/

from utils import TestRunner


class SolutionBrute:
    # TC: O(2^m*n)
    # SC: O(2^m*n)
    def uniquePaths(self, m, n):
        return self.solve(m, n, 0, 0)

    def solve(self, m, n, i, j):
        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        return self.solve(m, n, i + 1, j) + self.solve(m, n, i, j + 1)


class SolutionOptimal:
    # TC: O(m*n)
    # SC: O(m*n)
    def __init__(self) -> None:
        self.memo = {}

    def uniquePaths(self, m, n):
        return self.solve(m, n, 0, 0)

    def solve(self, m, n, i, j):
        if self.memo.get((i, j)):
            return self.memo.get((i, j))

        if i >= m or j >= n:
            return 0
        if i == m - 1 and j == n - 1:
            return 1

        ans = self.solve(m, n, i + 1, j) + self.solve(m, n, i, j + 1)
        self.memo[(i, j)] = ans
        return ans


class SolutionBest:
    # TC: O(m-1)
    # SC: O(1)
    def uniquePaths(self, m, n):
        N = m + n - 2
        r = m - 1
        ans = 1
        for i in range(1, r + 1):
            ans = ans * (N - r + i) / i
        return int(ans)


cases = [
    # (input, expected_output),
    ((3, 7), 28),
    ((3, 2), 3),
    ((2, 3), 3),
    ((2, 2), 2),
    ((1, 1), 1),
    ((4, 1), 1),
    ((5, 10), 715),
    ((13, 20), 141120525),
]

if __name__ == "__main__":
    TestRunner(SolutoinBest().uniquePaths).test(cases)
