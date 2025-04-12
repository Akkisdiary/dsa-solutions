# Rat in a Maze Problem - I
# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

from utils import TestRunner


class SolutionBrute:
    def findPath(self, m):
        n = len(m)
        ans = []
        moves = []
        visited = [[0] * n for _ in range(n)]

        def canVisit(i, j):
            if i < 0 or i >= n:
                return False
            if j < 0 or j >= n:
                return False
            if not m[i][j]:
                return False
            if visited[i][j]:
                return False
            return True

        def move(i, j):
            if not canVisit(i, j):
                return

            if i == n - 1 and j == n - 1:
                ans.append("".join(moves))
                return

            visited[i][j] = 1

            for mi, mj, d in [
                (i - 1, j, "U"),
                (i, j + 1, "R"),
                (i + 1, j, "D"),
                (i, j - 1, "L"),
            ]:
                moves.append(d)
                move(mi, mj)
                moves.pop(-1)

            visited[i][j] = 0

        move(0, 0)
        return ans


cases = [
    {"input": {"m": [[1, 0], [1, 1]]}, "expected": ["DR"]},
    {"input": {"m": [[1, 0], [1, 0]]}, "expected": []},
    {"input": {"m": [[0, 0], [1, 0]]}, "expected": []},
    {
        "input": {
            "m": [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
        },
        "expected": ["DDRDRR", "DRDDRR"],
    },
    {"input": {"m": [[1, 1], [1, 1]]}, "expected": ["DR", "RD"]},
    {
        "input": {
            "m": [[0, 1, 1, 1], [1, 1, 1, 0], [1, 0, 1, 1], [0, 0, 1, 1]]
        },
        "expected": [],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().findPath).test(cases, sorted)
