# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/description/

from utils import TestRunner


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ans = 0
        s = 0
        for i in nums:
            if i == 1:
                s += 1
            else:
                s = 0
            ans = max(ans, s)
        return ans


cases = [
    {"input": {"nums": [1, 1, 0, 1, 1, 1]}, "expected": 3},
    {"input": {"nums": [1, 0, 1, 1, 0, 1]}, "expected": 2},
    {"input": {"nums": [1, 1, 1, 1]}, "expected": 4},
    {"input": {"nums": [0, 0, 0, 0]}, "expected": 0},
    {"input": {"nums": [0, 0, 1]}, "expected": 1},
    {"input": {"nums": [1, 0, 0]}, "expected": 1},
    {"input": {"nums": []}, "expected": 0},
]

if __name__ == "__main__":
    TestRunner(Solution().findMaxConsecutiveOnes).test(cases)
