# Q. Find all the missing numbers in sorted array

arr = [1, 2, 3, 6, 9]


def find(arr, i, j):
    if len(arr) == 0:
        return []

    mid = (i + j) // 2

    if mid == i:
        return list(range(arr[i] + 1, arr[j]))

    ans = []
    if arr[mid] != mid + arr[0]:
        ans.extend(find(arr, i, mid))

    ans.extend(find(arr, mid, j))

    return ans


missing = find(arr, 0, len(arr) - 1)
print(missing)
