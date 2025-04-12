# 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/description/

from utils import TestRunner


class SolutionBrute:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = self.genPermutations(n)
        permutations.sort()
        return permutations[k - 1]

    def genPermutations(self, n):
        permutations = []
        opts = list(range(1, n + 1))

        def swap(i, j):
            opts[i], opts[j] = opts[j], opts[i]
            return opts

        def gen(start):
            if start >= n:
                permutations.append("".join(map(str, opts)))
                return
            for i in range(start, n):
                swap(start, i)
                gen(start + 1)
                swap(start, i)

        gen(0)
        return permutations


class SolutionOptimal:
    def getPermutation(self, n, k):
        nums = list(range(1, n + 1))
        fact = 1
        for i in range(1, n):
            fact *= i

        k = k - 1
        ans = ""
        while True:
            ans += str(nums[k // fact])
            nums.pop(k // fact)
            if len(nums) == 0:
                break
            k = k % fact
            fact = fact // len(nums)
        return ans


cases = [
    {"input": {"n": 3, "k": 3}, "expected": "213"},
    {"input": {"n": 4, "k": 9}, "expected": "2314"},
    {"input": {"n": 3, "k": 1}, "expected": "123"},
    {"input": {"n": 9, "k": 305645}, "expected": "856412937"},
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().getPermutation).test(cases)
