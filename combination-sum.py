# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from utils import TestRunner


class Solution:
    def combinationSum(self, candidates, target):
        ans = []

        def solve(i, t, subset):
            if t == 0:
                ans.append(list(subset))
                return
            if i < len(candidates):
                if candidates[i] <= t:
                    solve(i, t-candidates[i], subset + [candidates[i]])
                solve(i+1, t, list(subset))

        solve(0, target, [])
        return ans


cases = [
    {
        "input": {
            "candidates": [2, 3, 6, 7],
            "target": 7,
        },
        "expected": [[2, 2, 3], [7]],
    },
    {
        "input": {
            "candidates": [2, 3, 5],
            "target": 8,
        },
        "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
    },
    {
        "input": {
            "candidates": [2],
            "target": 1,
        },
        "expected": [],
    },
]

if __name__ == "__main__":
    TestRunner(Solution().combinationSum).test(cases)
