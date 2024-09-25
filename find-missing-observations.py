# 2028. Find Missing Observations
# https://leetcode.com/problems/find-missing-observations/description

from utils import TestRunner


class Solution:
    def missingRolls(self, rolls, mean, n):
        nx = (len(rolls) + n) * mean - sum(rolls)
        sub = 0
        while nx > 0 and nx % n != 0:
            sub += 1
            nx -= 1
        x = nx // n

        if 0 >= x or x > 6 or (sub and x >= 6):
            return []
        return [int(x)] * (n - sub) + [int(x) + 1] * sub


test_cases = [
    {
        "input": {
            "rolls": [3, 2, 4, 3],
            "mean": 4,
            "n": 2,
        },
        "expected": [6, 6],
    },
    {
        "input": {
            "rolls": [1, 5, 6],
            "mean": 3,
            "n": 4,
        },
        "expected": [2, 2, 2, 3],
    },
    {
        "input": {
            "rolls": [1, 2, 3, 4],
            "mean": 6,
            "n": 4,
        },
        "expected": [],
    },
    {
        "input": {
            "rolls": [1, 5, 6, 2, 3],
            "mean": 4,
            "n": 2,
        },
        "expected": [6, 5],
    },
    {
        "input": {
            "rolls": [6, 3, 4, 3, 5, 3],
            "mean": 1,
            "n": 6,
        },
        "expected": [],
    },
    {
        "input": {
            "rolls": [6, 1, 5, 2],
            "mean": 4,
            "n": 4,
        },
        "expected": [5, 4, 4, 5],
    },
    {
        "input": {
            "rolls": [3, 5, 3],
            "mean": 5,
            "n": 3,
        },
        "expected": [],
    },
]
for case in test_cases:
    TestRunner(
        Solution().missingRolls,
    ).case(
        case
    ).test(lambda x: list(sorted(x)))
