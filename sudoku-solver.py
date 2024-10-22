# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/

from utils import TestRunner


class Solution:
    def solveSudoku(self, board):
        def isValid(row, col, digit):
            for i in range(9):
                if any((
                    board[row][i] == digit,
                    board[i][col] == digit,
                    board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == digit,
                )):
                    return False
            return True

        def solve():
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for digit in "123456789":
                            if isValid(i, j, digit):
                                board[i][j] = digit
                                if solve():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        solve()
        return board


cases = [
    {
        "input": {
            "board": [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"]
            ],
        },
        "expected": [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
    },
]

if __name__ == "__main__":
    TestRunner(Solution().solveSudoku).test(cases)
