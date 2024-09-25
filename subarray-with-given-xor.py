# Subarray with given XOR
# https://www.interviewbit.com/problems/subarray-with-given-xor/

from utils import TestRunner


class SolutionBrute:
    def solve(self, A, B):
        count = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                if self.get_xor(A, i, j) == B:
                    count += 1
        return count

    def get_xor(self, A, i, j):
        ans = 0
        while i <= j:
            ans = ans ^ A[i]
            i += 1
        return ans


class SolutionOptimal:
    def solve(self, A, B):
        count = 0
        memo = {}
        prev = 0
        for a in A:
            xor = prev ^ a
            if xor == B:
                count += 1
            count += memo.get(xor ^ B, 0)
            memo[xor] = memo.get(xor, 0) + 1
            prev = xor
        return count


test_cases = [
    {
        "input": {
            "A": [4, 2, 2, 6, 4],
            "B": 6,
        },
        "expected": 4,
    },
    {
        "input": {
            "A": [0, 4, 2, 6, 2, 6, 4],
            "B": 6,
        },
        "expected": 6,
    },
    {
        "input": {
            "A": [5, 6, 7, 8, 9],
            "B": 5,
        },
        "expected": 2,
    },
]
for case in test_cases:
    TestRunner(SolutionOptimal().solve).case(case).test()
