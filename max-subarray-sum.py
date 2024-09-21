# Max sub array sum
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxi = nums[0]
    currSum = 0

    for n in nums:
        currSum += n
        maxi = max(currSum, maxi)

        if currSum < 0:
            currSum = 0

    return maxi


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
