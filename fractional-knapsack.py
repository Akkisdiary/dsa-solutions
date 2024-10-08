# Fractional Knapsack
# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

from utils import TestRunner


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w

    def _str(self):
        return f"Item({self.value}, {self.weight})"

    def __str__(self) -> str:
        return self._str()

    def __repr__(self) -> str:
        return self._str()


class Solution:
    def fractionalKnapsack(self, w, arr, n):
        arr.sort(key=lambda i: (i.value/i.weight), reverse=True)
        value = i = 0
        while w > 0 and i < n:
            item = arr[i]
            if item.weight <= w:
                value += item.value
                w -= item.weight
            else:
                value += (item.value/item.weight) * w
                w -= w
            i += 1
        return value


cases = [
    {
        "input": {
            "arr": [Item(60, 10), Item(100, 20), Item(120, 30)],
            "w": 50,
            "n": 3,
        },
        "expected": 240.000000,
    },
    {
        "input": {
            "arr": [Item(60, 10), Item(100, 20)],
            "w": 50,
            "n": 2,
        },
        "expected": 160.000000,
    },
]

if __name__ == "__main__":
    TestRunner(Solution().fractionalKnapsack).test(cases)
