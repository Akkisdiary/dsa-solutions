# Count Subarrays with Given XOR

# https://www.codingninjas.com/codestudio/problems/1115652?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website


def subarraysXor(arr, x):
    count = 0

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            xor = 0
            for e in arr[i:j]:
                xor = xor ^ e
            if xor == x:
                count += 1
    return count


print(subarraysXor([10, 1, 0, 3, 4, 7], 11))
