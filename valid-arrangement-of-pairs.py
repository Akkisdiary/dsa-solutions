"""
2097. Valid Arrangement of Pairs
https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-11-30
"""

from typing import List

from utils import TestRunner


class SolutionBrute:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        arrangement = []
        taken = [0] * len(pairs)
        print(pairs)

        def can_take(i):
            if taken[i]:
                return False
            if len(arrangement) == 0:
                return True
            return arrangement[-1][1] == pairs[i][0]

        def solve():
            print(arrangement)
            if len(arrangement) == len(pairs):
                return True
            for i in range(len(pairs)):
                if can_take(i):
                    taken[i] = 1
                    arrangement.append(pairs[i])
                    if solve():
                        return True
                    arrangement.pop(-1)
                    taken[i] = 0
            return False

        solve()
        return arrangement


cases = [
    {
        "input": {"pairs": [[5, 1], [4, 5], [11, 9], [9, 4]]},
        "expected": [[11, 9], [9, 4], [4, 5], [5, 1]],
    },
    {
        "input": {"pairs": [[1, 3], [3, 2], [2, 1]]},
        "expected": [[1, 3], [3, 2], [2, 1]],
    },
    {
        "input": {"pairs": [[1, 2], [1, 3], [2, 1]]},
        "expected": [[1, 2], [2, 1], [1, 3]],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().validArrangement).test(cases)
