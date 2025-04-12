# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/description/

from utils import TestRunner


class SolutionBrute:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        for i in range(len(n)):
            maxi = i
            for j in range(len(n) - 1, i, -1):
                if n[maxi] < n[j]:
                    maxi = j
            if maxi != i:
                n[i], n[maxi] = n[maxi], n[i]
                return int("".join(n))
        return int("".join(n))


cases = [
    {"input": {"num": 2736}, "expected": 7236},
    {"input": {"num": 9973}, "expected": 9973},
    {"input": {"num": 8345}, "expected": 8543},
    {"input": {"num": 8345}, "expected": 8543},
    {"input": {"num": 1993}, "expected": 9913},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().maximumSwap).test(cases)
