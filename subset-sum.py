# Subset Sum

# https://www.codingninjas.com/codestudio/problems/subset-sum_3843086?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website


def subsetSum(nums):
    n = len(nums)

    subsetSums = [0]

    def findSubsets(i, prevSum):
        if i >= n:
            return

        findSubsets(i + 1, prevSum)
        # findSubsets(i+1, nums[i])
        findSubsets(i + 1, prevSum + nums[i])

        subsetSums.append(prevSum + nums[i])

    findSubsets(0, 0)

    subsetSums.sort()
    return subsetSums


print(subsetSum([1, 2, 3]))
