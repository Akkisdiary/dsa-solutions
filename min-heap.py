"""
Min Heap
https://www.naukri.com/code360/problems/min-heap_4691801
"""

from typing import List

from utils import TestRunner


class MinHeap:
    def __init__(self):
        self.length = 0
        self.heap = [None]

    def insert(self, element):
        self.heap[self.length] = element
        self.heap.append(None)
        self.length += 1

        i = self.length - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def pop(self):
        ans = None

        if self.length > 0:
            ans = self.heap[0]
            self.length -= 1
            self.heap[0], self.heap[self.length] = self.heap[self.length], None
            self.heap.pop(-1)

            i = 0
            while i <= self.length:
                child = -1
                left = (2 * i) + 1
                right = (2 * i) + 2

                if left < self.length:
                    child = left

                if right < self.length and self.heap[right] < self.heap[left]:
                    child = right

                if child >= 0 and self.heap[i] > self.heap[child]:
                    self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
                    i = child
                else:
                    break
        return ans


class Solution:
    def minHeap(self, N: int, Q: List[List[int]]) -> List[int]:
        ans = []
        heap = MinHeap()
        for op in Q:
            if len(op) > 1:
                heap.insert(op[1])
            else:
                ans.append(heap.pop())
        return ans


cases = [
    {
        "input": {
            "N": 3,
            "Q": [[0, 2], [0, 1], [1]],
        },
        "expected": [1]
    },
    {
        "input": {
            "N": 2,
            "Q": [[0, 1], [1]],
        },
        "expected": [1],
    },
    {
        "input": {
            "N": 6,
            "Q": [
                [0, 1], [0, 4], [0, 3], [0, 0], [0, 3], [0, 1],
                [1], [1], [1], [1], [1], [1],
            ],
        },
        "expected": [0, 1, 1, 3, 3, 4],
    },
    {
        "input": {
            "N": 10,
            "Q": [
                [0, 32], [1,], [0, 30], [0, 48], [0, 13],
                [1,], [0, 10], [1,], [0, 8], [0, 38],
            ],
        },
        "expected": [32, 13, 10],
    },
    {
        "input": {
            "N": 4,
            "Q": [
                [0, 14], [1,],
                [0, 27], [0, 39],
            ],
        },
        "expected": [14],
    },
]

if __name__ == "__main__":
    TestRunner(Solution().minHeap).test(cases)
