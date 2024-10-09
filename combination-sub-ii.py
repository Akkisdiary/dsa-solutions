# 39. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/description/

from utils import TestRunner


class SolutionBrute:
    def combinationSum2(self, candidates, target):
        ans = set()

        def solve(i, t, subset):
            if t == 0:
                ans.add(tuple(subset))
                return
            if i < len(candidates):
                if candidates[i] <= t:
                    solve(i + 1, t - candidates[i], subset + [candidates[i]])
                solve(i + 1, t, list(subset))

        candidates.sort()
        solve(0, target, [])
        return list(map(list, ans))


class SolutionOptimal:
    def combinationSum2(self, candidates, target):
        ans = []
        ds = []
        candidates.sort()

        def solve(idx, t):
            if t == 0:
                ans.append(list(ds))
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > t:
                    break
                ds.append(candidates[i])
                solve(i + 1, t - candidates[i])
                ds.pop()
        solve(0, target)
        return ans


cases = [
    {
        "input": {
            "candidates": [10, 1, 2, 7, 6, 1, 5],
            "target": 8,
        },
        "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
    },
    {
        "input": {
            "candidates": [2, 5, 2, 1, 2],
            "target": 5,
        },
        "expected": [[1, 2, 2], [5]],
    },
    {
        "input": {
            "candidates": [1] * 10,
            "target": 2,
        },
        "expected": [[1]*2],
    },
    {
        "input": {
            "candidates": [
                14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16,
                12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30,
                12, 33, 20, 21, 29, 24, 17, 27, 34, 11, 17,
                30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28,
                11, 33, 10, 32, 22, 13, 34, 18, 12
            ],
            "target": 27,
        },
        "expected": [
            [6, 6, 7, 8], [6, 7, 14], [6, 8, 13], [6, 9, 12],
            [6, 10, 11], [6, 21], [7, 8, 12], [7, 9, 11], [7, 20],
            [8, 8, 11], [8, 9, 10], [9, 9, 9], [9, 18], [10, 17],
            [11, 16], [13, 14], [27]
        ],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().combinationSum2).test(cases, sorted)
