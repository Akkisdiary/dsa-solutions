# Subset Sum
# https://www.geeksforgeeks.org/problems/subset-sums2234/1
# https://www.codingninjas.com/codestudio/problems/subset-sum_3843086

from utils import TestRunner


class SolutionBrute:
    def subsetsWithDup(self, nums):
        ans = self.solve(nums, 0, [], [])
        return self.removeDuplicates(ans)

    def solve(self, nums, i, ans, subset):
        if i == len(nums):
            ans.append(subset)
            return ans
        self.solve(nums, i + 1, ans, subset + [])
        self.solve(nums, i + 1, ans, subset + [nums[i]])
        return ans

    def removeDuplicates(self, ans):
        ans = map(tuple, ans)
        ans = set(ans)
        ans = map(list, ans)
        return list(sorted(ans))


class SolutionOptimal:
    def subsetsWithDup(self, nums):
        nums.sort()
        print(nums)
        return self.solve(nums, 0, [], [])

    def solve(self, nums, index, ans, subset):
        ans.append(list(subset))
        if index == len(nums):
            return ans
        for i in range(index, len(nums)):
            if i == index:
                self.solve(nums, i + 1, ans, subset + [nums[i]])
            elif nums[i] != nums[i - 1]:
                self.solve(nums, i + 1, ans, subset + [nums[i]])
        return ans


test_cases = [
    {
        "input": {
            "nums": [1, 2, 2],
        },
        "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
    },
    {
        "input": {
            "nums": [0],
        },
        "expected": [[], [0]],
    },
    {
        "input": {
            "nums": [],
        },
        "expected": [[]],
    },
    {
        "input": {
            "nums": [4, 4, 4, 1, 4],
        },
        "expected": [
            [],
            [1],
            [1, 4],
            [1, 4, 4],
            [1, 4, 4, 4],
            [1, 4, 4, 4, 4],
            [4],
            [4, 4],
            [4, 4, 4],
            [4, 4, 4, 4],
        ],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionOptimal().subsetsWithDup, test_cases).test(sorted)
