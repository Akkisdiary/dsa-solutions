# 1128. Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from collections import defaultdict
from typing import List

from utils import TestRunner


class SolutionBrute:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        memo = defaultdict(int)
        for i in range(n):
            for j in range(i + 1, n):
                d1 = sorted(dominoes[i])
                d2 = sorted(dominoes[j])
                if d1 == d2:
                    memo[tuple(d1)] += 1
        return sum(memo.values())


class SolutionBetter:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        memo = defaultdict(int)
        for d in dominoes:
            if d[0] < d[1]:
                memo[(d[0], d[1])] += 1
            else:
                memo[(d[1], d[0])] += 1
        ans = 0
        for v in memo.values():
            ans += ((v - 1) * v) // 2
        return ans


cases = [
    {"input": {"dominoes": [[1, 2], [2, 1], [3, 4], [5, 6]]}, "expected": 1},
    {
        "input": {"dominoes": [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]},
        "expected": 3,
    },
    {
        "input": {"dominoes": [[1, 2], [1, 2], [1, 2], [1, 2], [2, 2]]},
        "expected": 6,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().numEquivDominoPairs).test(cases)
