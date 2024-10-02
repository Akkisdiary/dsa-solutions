# 42. Trapping Rain Water
# https://www.codingninjas.com/codestudio/problems/630519
# https://leetcode.com/problems/trapping-rain-water/description/

from utils import TestRunner


def getTrappedWater(height):
    n = len(height)
    if n < 3:
        return 0

    leftPeak = 0
    rightPeak = n - 1

    while leftPeak < n - 1 and height[leftPeak] <= height[leftPeak + 1]:
        leftPeak += 1
    while rightPeak > 1 and height[rightPeak] <= height[rightPeak - 1]:
        rightPeak -= 1

    trappedWater = 0

    while leftPeak < rightPeak:
        nextPeak = leftPeak + 1
        while nextPeak < rightPeak and height[nextPeak] < height[leftPeak]:
            nextPeak += 1

        i = leftPeak + 1
        while i < nextPeak:
            trappedWater += min(height[leftPeak], height[nextPeak]) - min(
                height[i], height[nextPeak]
            )
            i += 1

        leftPeak = nextPeak

    return trappedWater


class SolutionBrute:
    def trap(self, height):
        water = mid = 0
        left = height[0]
        right = height[-1]
        n = len(height)

        i = 1
        j = n - 2
        while mid < n:
            i = j = mid
            left = right = height[mid]
            while 0 <= i:
                left = max(left, height[i])
                i -= 1
            while j < n:
                right = max(right, height[j])
                j += 1
            if height[mid] < min(left, right):
                water += min(left, right) - height[mid]
            mid += 1

        return water


class SolutionBetter:
    def trap(self, height):
        water = i = 0
        j = len(height) - 1
        left = height[i]
        right = height[j]

        while i < j:
            if height[i] <= height[j]:
                while i < j and height[i] <= height[j]:
                    if height[i] < min(left, right):
                        water += min(left, right) - height[i]
                    i += 1
                    left = max(left, height[i])
            else:
                while i < j and height[i] >= height[j]:
                    if height[j] < min(left, right):
                        water += min(left, right) - height[j]
                    j -= 1
                    right = max(right, height[j])

        return water


test_cases = [
    {
        "input": {
            "height": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        },
        "expected": 6,
    },
    {
        "input": {
            "height": [4, 2, 0, 3, 2, 5],
        },
        "expected": 9,
    },
    {
        "input": {
            "height": [3, 0, 0, 2, 0, 4],
        },
        "expected": 10,
    },
    {
        "input": {
            "height": [2, 1, 1, 4],
        },
        "expected": 2,
    },
    {
        "input": {
            "height": [8, 1, 8, 2, 4],
        },
        "expected": 9,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().trap, test_cases).test()
