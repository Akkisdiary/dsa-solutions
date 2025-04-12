# 18. Four Sum
# https://leetcode.com/problems/4sum/

from utils import TestRunner


class SolutionBrute(object):
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ans.append([nums[i], nums[j], nums[k], nums[l]])
        return ans


class SolutionBetter(object):
    def fourSum(self, nums, target):
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                memo = set()
                for k in range(j + 1, n):
                    diff = target - (nums[i] + nums[j] + nums[k])
                    if diff in memo:
                        ans.append([nums[i], nums[j], nums[k], diff])
                    memo.add(nums[k])
        return ans


class SolutionOptimal(object):
    def fourSum(self, nums, target):
        ans = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                k = j + 1
                l = n - 1
                while j < k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k = self.get_next(nums, k, 1)
                        l = self.get_next(nums, l, -1)
                    elif s < target:
                        k += 1
                    else:
                        l -= 1
                j = self.get_next(nums, j, 1)
            i = self.get_next(nums, i, 1)
        return ans

    def get_next(self, nums, index, incr=1):
        index += incr
        while 0 < index < len(nums) and nums[index] == nums[index - incr]:
            index += incr
        return index


cases = [
    {
        "input": {"nums": [1, 0, -1, 0, -2, 2], "target": 0},
        "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
    },
    {
        "input": {"nums": [2, 2, 2, 2, 2], "target": 8},
        "expected": [[2, 2, 2, 2]],
    },
    {"input": {"nums": [1, 5, 6, 3], "target": 13}, "expected": []},
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().fourSum).test(
        cases, lambda x: list(map(lambda i: tuple(sorted(i)), x))
    )
