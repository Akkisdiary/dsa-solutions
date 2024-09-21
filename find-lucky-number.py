import typing


def findLuckyNum(arr: typing.List[int]):
    while len(arr) > 0:
        if len(arr) == 1:
            return arr[0]

        mini = arr.pop(0)
        maxi = arr.pop(-1)

        diff = maxi - mini
        if diff not in arr:
            arr.append(diff)


print(findLuckyNum([3, 2, 4, 5, 6, 8]))
