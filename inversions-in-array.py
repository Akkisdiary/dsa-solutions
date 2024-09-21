# Q. Inversions in Array


def merge(arr, start, mid, end):
    """
    2 3 1
    s   m,e
    """
    inversions = 0

    if start >= end:
        return inversions

    while start < mid <= end:
        if arr[mid] < arr[start]:
            arr.insert(start, arr.pop(mid))
            inversions += mid - start
            mid += 1
        start += 1

    return inversions


def solve(arr, inversions, start, end):
    """
    3 2 1
    """
    if start >= end:
        return inversions

    mid = (start + end) // 2
    inversions += solve(arr, 0, start, mid)
    inversions += solve(arr, 0, mid + 1, end)

    inversions += merge(arr, start, mid + 1, end)

    return inversions


def getInversions(arr, n):
    return solve(arr, 0, 0, n - 1)


getInversions([3, 2, 1], 3)
