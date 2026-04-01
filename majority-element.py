# 169. Majority Element
# https://leetcode.com/problems/majority-element/

from utils import TestRunner


class SolutionBrute:
    def majorityElement(self, nums):
        memo = {}
        for n in nums:
            memo[n] = memo.get(n, 0) + 1

        for n, c in memo.items():
            if c > len(nums) / 2:
                return n


class SolutionOptimal:
    def majorityElement(self, nums):
        n = nums[0]
        c = 1
        for i in range(1, len(nums)):
            if nums[i] == n:
                c += 1
            elif c == 0:
                n = nums[i]
                c += 1
            else:
                c -= 1
        return n


cases = [
    {
        "input": {"nums": [3, 2, 3]},
        "expected": 3,
    },
    {
        "input": {"nums": [2, 2, 1, 1, 1, 2, 2]},
        "expected": 2,
    }
]
if __name__ == "__main__":
    TestRunner(SolutionBrute().majorityElement).test(cases)
    TestRunner(SolutionOptimal().majorityElement).test(cases)
