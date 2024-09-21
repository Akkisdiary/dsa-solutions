# Trapping Rain Water


# https://www.codingninjas.com/codestudio/problems/630519?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
def getTrappedWater(arr, n):
    if n < 3:
        return 0

    leftPeak = 0
    rightPeak = n - 1

    while leftPeak < n - 1 and arr[leftPeak] <= arr[leftPeak + 1]:
        leftPeak += 1
    while rightPeak > 1 and arr[rightPeak] <= arr[rightPeak - 1]:
        rightPeak -= 1

    trappedWater = 0

    while leftPeak < rightPeak:
        nextPeak = leftPeak + 1
        while nextPeak < rightPeak and arr[nextPeak] < arr[leftPeak]:
            nextPeak += 1

        i = leftPeak + 1
        while i < nextPeak:
            trappedWater += min(arr[leftPeak], arr[nextPeak]) - min(
                arr[i], arr[nextPeak]
            )
            i += 1

        leftPeak = nextPeak

    return trappedWater


print(getTrappedWater([9, 6, 8, 8, 5, 6, 3], 7))
