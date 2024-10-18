# 46. Permutations
# https://leetcode.com/problems/permutations/description/

from utils import TestRunner


class SolutionBrute:
    def permute(self, nums):
        permutations = []

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def gen(index):
            if index == len(nums):
                permutations.append(nums[:])
                return
            for i in range(index, len(nums)):
                swap(index, i)
                gen(index+1)
                swap(index, i)

        gen(0)
        print(permutations)
        return permutations


cases = [
    {
        "input": {
            "nums": [1]
        },
        "expected": [[1]]
    },
    {
        "input": {
            "nums": [0, 1]
        },
        "expected": [[0, 1], [1, 0]]
    },
    {
        "input": {"nums": [1, 2, 3]},
        "expected": [
            [1, 2, 3], [1, 3, 2], [2, 1, 3],
            [2, 3, 1], [3, 1, 2], [3, 2, 1]
        ],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().permute).test(cases, sorted)
