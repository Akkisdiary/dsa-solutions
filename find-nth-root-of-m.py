"""
Find Nth Root Of M
https://www.naukri.com/code360/problems/1062679
"""

from utils import TestRunner


class SolutionBrute:
    def NthRoot(self, n: int, m: int):
        for i in range(m + 1):
            a = i**n
            if a > m:
                return -1
            if a == m:
                return i
        return -1


class SolutionOptimal:
    def NthRoot(self, n: int, m: int):
        low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2
            midN = mid ** n
            if midN == m:
                return mid
            if midN > m:
                high = mid - 1
            else:
                low = mid + 1
        return -1


cases = [
    {
        "input": {"n": 3, "m": 27},
        "expected": 3,
    },
    {
        "input": {"n": 69, "m": 4},
        "expected": -1,
    },
    {
        "input": {"n": 9, "m": 1953125},
        "expected": 5,
    },
    {
        "input": {"n": 8, "m": 214358881},
        "expected": 11,
    },

]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().NthRoot).test(cases)
