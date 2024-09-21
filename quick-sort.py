# Quick Sort - https://practice.geeksforgeeks.org/problems/quick-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=quick-sort


class Solution:
    # { 4, 1, 3, 9, 7 }
    # { 2, 1, 6, 10, 4, 1, 3, 9, 7 }
    def quickSort(self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = high
        i = low
        j = high

        while i < j:
            while i < j and arr[i] <= arr[pivot]:
                i += 1
            while j > i and arr[j] >= arr[pivot]:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[j], arr[pivot] = arr[pivot], arr[j]

        return j


arr = [2, 1, 6, 10, 4, 1, 3, 9, 7]
print(arr)
Solution().quickSort(arr, 0, len(arr) - 1)
print(arr)
