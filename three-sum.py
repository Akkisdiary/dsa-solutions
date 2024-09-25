# Three sum
# https://www.naukri.com/code360/problems/three-sum_6922132

from utils import TestRunner


class SolutionBrute:
    def triplet(n, arr):
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] == 0:
                        ans.append([arr[i], arr[j], arr[k]])
        return ans


class SolutionBetter:
    def triplet(self, n, arr):
        ans = []
        for i in range(n):
            memo = set()
            for j in range(i + 1, n):
                diff = 0 - (arr[i] + arr[j])
                if diff in memo:
                    ans.append([arr[i], arr[j], diff])
                memo.add(arr[j])
        return ans


class SolutionOptimal:
    def triplet(self, n, arr):
        arr.sort()
        i = 0
        ans = []
        while i < n:
            j = i + 1
            k = n - 1
            while i < j < k:
                s = arr[i] + arr[j] + arr[k]
                if s == 0:
                    ans.append([arr[i], arr[j], arr[k]])
                    j += 1
                    while i < j < k and arr[j] == arr[j-1]:
                        j += 1
                    k -= 1
                    while i < j < k < n-1 and arr[k] == arr[k+1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
            while i < n and arr[i] == arr[i-1]:
                i += 1
        return ans


test_cases = [
    {
        "input": {
            "arr": [-1, -1, 2, 0, 1],
            "n": 5,
        },
        "expected": [[-1, -1, 2], [-1, 0, 1]],
    },
    {
        "input": {
            "arr": [0, 0, 0, 0],
            "n": 4,
        },
        "expected": [[0, 0, 0]],
    },
    {
        "input": {
            "arr": [1, 5, 6, 3],
            "n": 4,
        },
        "expected": [],
    },
]
for case in test_cases:
    TestRunner(SolutionOptimal().triplet).case(case).test(
        lambda x: list(map(lambda i: tuple(sorted(i)), x))
    )
