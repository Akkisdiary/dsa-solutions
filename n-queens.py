# 51. N-Queens
# https://leetcode.com/problems/n-queens/description/

from utils import TestRunner


class SolutionBrute:
    def solveNQueens(self, n):
        ans = []
        board = []
        for _ in range(n):
            board.append([0]*n)

        def renderAns():
            b = []
            for r in board:
                rs = ""
                for c in r:
                    if c:
                        rs += "Q"
                    else:
                        rs += "."
                b.append(rs)
            return b

        def isSafe(row, col):
            dr = row
            dc = col
            while row >= 0:
                if board[row][col]:
                    return False
                row -= 1
            row = dr
            col = dc
            while row >= 0 and col >= 0:
                if board[row][col]:
                    return False
                row -= 1
                col -= 1
            row = dr
            col = dc
            while row >= 0 and col < n:
                if board[row][col]:
                    return False
                row -= 1
                col += 1
            return True

        def solve(row):
            if row == n:
                ans.append(renderAns())
                return
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 1
                    solve(row + 1)
                    board[row][col] = 0
        solve(0)
        return ans


cases = [
    {"input": {"n": 1}, "expected": [["Q"]]},
    {"input": {"n": 2}, "expected": []},
    {"input": {"n": 3}, "expected": []},
    {
        "input": {"n": 4},
        "expected": [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."],
        ],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().solveNQueens).test(cases)
