# Longest sub array with zero sum
# https://www.codingninjas.com/codestudio/problems/920321?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

from utils import TestRunner


class SolutionBrute:
    def maxLen(self, n, arr):
        maxi = 0
        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                if sum(arr[i : j + 1]) == 0:
                    maxi = max(maxi, j - i + 1)
        return maxi


class SolutionOptimal:
    def maxLen(self, n, arr):
        maxi = 0
        lastSum = 0
        prefixSum = {}
        for i in range(n):
            lastSum += arr[i]
            if lastSum == 0:
                maxi = i + 1
            if lastSum in prefixSum:
                maxi = max(i - prefixSum[lastSum], maxi)
            else:
                prefixSum[lastSum] = i
        return maxi


cases = [
    {"input": {"arr": [15, -2, 2, -8, 1, 7, 10, 23], "n": 8}, "expected": 5},
    {"input": {"arr": [2, 10, 4], "n": 3}, "expected": 0},
    {"input": {"arr": [1, 0, -4, 3, 1, 0], "n": 6}, "expected": 5},
    {"input": {"arr": [0, 0, 0, 0, 0, 0], "n": 6}, "expected": 6},
    {"input": {"arr": [0, 0, -1, 1, 0, 0], "n": 6}, "expected": 6},
    {"input": {"arr": [2, 0, -1, 1, 0, 4], "n": 6}, "expected": 4},
    {"input": {"arr": [0, -1, 1, 3, 0, 4, -4, -5, 6], "n": 9}, "expected": 3},
    {
        "input": {"arr": [-3, -1, 1, 3, 6, 0, 4, -4, -5, 6], "n": 10},
        "expected": 4,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().maxLen).test(cases)
