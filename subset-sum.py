# Subset Sum
# Subset Sum
# https://www.geeksforgeeks.org/problems/subset-sums2234/1
# https://www.codingninjas.com/codestudio/problems/subset-sum_3843086

from utils import TestRunner


class SolutionBrute:
    def subsetSums(self, arr, n):
        return self.solve(arr, n, 0, [], 0)

    def solve(self, arr, n, i, ans, rsum):
        if i == n:
            ans.append(rsum)
            return ans
        self.solve(arr, n, i+1, ans, rsum)
        self.solve(arr, n, i+1, ans, rsum+arr[i])
        return ans


test_cases = [
    {
        "input": {
            "arr": [2, 3],
            "n": 2,
        },
        "expected": [0, 2, 3, 5],
    },
    {
        "input": {
            "arr": [1, 2, 1],
            "n": 3,
        },
        "expected": [0, 1, 1, 2, 2, 3, 3, 4],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().subsetSums, test_cases).test(sorted)
