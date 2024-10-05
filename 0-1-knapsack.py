# Fractional Knapsack
# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

from utils import TestRunner


class SolutionBrute:
    def knapSack(self, W, wt, val):
        return self.solve(W, wt, val, 0, 0)

    def solve(self, W, wt, val, i, value):
        if W == 0 or i >= len(wt):
            return value

        v1 = self.solve(W, wt, val, i+1, value)
        if wt[i] > W:
            return v1

        return max(
            v1,
            self.solve(W-wt[i], wt, val, i+1, value+val[i]),
        )


test_cases = [
    {
        "input": {
            "W": 4,
            "val": [1, 2, 3],
            "wt": [4, 5, 1],
        },
        "expected": 3,
    },
    {
        "input": {
            "W": 3,
            "val": [1, 2, 3],
            "wt": [4, 5, 6],
        },
        "expected": 0,
    },
    {
        "input": {
            "W": 87,
            "val": [
                61, 79, 80, 71, 89, 67, 70, 89, 56, 56, 68, 85, 84, 81, 58,
                83, 59, 55, 67, 58, 51, 72, 53, 79, 62, 51, 60, 88, 76, 76,
                78, 89, 63, 78, 85, 80, 80, 73, 60, 58, 70, 88, 56, 61, 71,
                77, 55, 86, 61, 61, 85, 87, 55, 51, 80, 76, 62, 54, 61, 66,
                78, 76, 59, 61, 54, 54, 64, 83, 86, 71, 88, 90, 73, 57, 84,
                68, 77, 59, 84, 67, 82, 58, 56, 70, 83, 54, 67, 57, 59, 60,
                66, 83, 50, 87, 72, 80
            ],
            "wt": [
                58, 59, 71, 77, 82, 63, 50, 81, 82, 68, 61, 79, 60, 84, 68,
                78, 60, 77, 82, 71, 57, 60, 55, 84, 72, 83, 53, 59, 80, 72,
                77, 55, 52, 60, 72, 71, 73, 84, 84, 61, 84, 73, 86, 57, 81,
                74, 71, 87, 58, 84, 58, 59, 66, 76, 51, 59, 86, 76, 61, 70,
                83, 51, 58, 50, 61, 62, 83, 63, 54, 58, 73, 69, 86, 86, 79,
                75, 65, 81, 61, 56, 51, 59, 86, 72, 87, 83, 79, 83, 83, 89,
                89, 85, 79, 84, 80, 79
            ],
        },
        "expected": 90,
    },
    {
        "input": {
            "W": 10,
            "val": [20, 11, 11],
            "wt": [9, 5, 5],
        },
        "expected": 22,
    },
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().knapSack, test_cases).test()
