# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from utils import TestRunner


class SolutionBrute:
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 1
        k = n - 1
        while i <= k:
            if nums[i] == nums[i - 1]:
                k = self.left_shift(nums, i, k)
            else:
                i += 1
        return k + 1

    def left_shift(self, nums, i, k):
        while i < k:
            nums[i] = nums[i + 1]
            i += 1
        nums[i] = None
        return k - 1


class SolutionBetter:
    def removeDuplicates(self, nums):
        s = list(set(nums))
        s.sort()
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)


class SolutionBetter2:
    def removeDuplicates(self, nums):
        ans = [nums[0]]
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                ans.append(nums[i])
            i += 1
        k = len(ans)
        for i in range(k):
            nums[i] = ans[i]
        return k


class SolutionOptimal:
    def removeDuplicates(self, nums):
        i = j = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j


cases = [
    {"input": {"nums": [1, 1, 2]}, "expected": [1, 2]},
    {
        "input": {"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]},
        "expected": [0, 1, 2, 3, 4],
    },
    {
        "input": {
            "nums": [-50, -50, -50, -45, -45, -45, -30, -30, -30, -25, -25, -25]
        },
        "expected": [-50, -45, -30, -25],
    },
]

# TODO: Figure out tests
# if __name__ == "__main__":
#     TestRunner(SolutionOptimal().removeDuplicates).test(cases)
