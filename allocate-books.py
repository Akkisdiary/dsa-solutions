"""
Allocate Books
https://www.interviewbit.com/problems/allocate-books/
"""

from utils import TestRunner


class SolutionBrute:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A):
            return -1

        partitions = []
        part = []

        def solve(start, students):
            if start == len(A) and students == 0:
                partitions.append(part[:])
                return
            for i in range(start, len(A)):
                part.append(A[start : i + 1])
                solve(i + 1, students - 1)
                part.pop(-1)

        solve(0, B)

        for i in range(len(partitions)):
            partitions[i] = list(map(sum, partitions[i]))

        ans = float("inf")
        for part in partitions:
            ans = min(ans, max(part))
        return ans


class SolutionOptimal:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B > len(A):
            return -1
        low, high = min(A), sum(A)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            students = self.allocate(A, mid)
            if students <= B:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def allocate(self, books, limit):
        ans = cur_pages = 0
        students = 1
        for pages in books:
            if pages > limit:
                return float("inf")
            if cur_pages + pages <= limit:
                cur_pages += pages
            else:
                students += 1
                cur_pages = pages
            ans = max(students, ans)
        return ans


cases = [
    {"input": {"A": [12, 12], "B": 2}, "expected": 12},
    {"input": {"A": [10], "B": 1}, "expected": 10},
    {"input": {"A": [10, 20, 1, 30], "B": 1}, "expected": 61},
    {"input": {"A": [12, 34, 67, 90], "B": 2}, "expected": 113},
    {"input": {"A": [5, 17, 100, 11], "B": 4}, "expected": 100},
    {"input": {"A": [5], "B": 2}, "expected": -1},
    {
        "input": {
            "A": [
                97,
                26,
                12,
                67,
                10,
                33,
                79,
                49,
                79,
                21,
                67,
                72,
                93,
                36,
                85,
                45,
                28,
                91,
                94,
                57,
                1,
                53,
                8,
                44,
                68,
                90,
                24,
            ],
            "B": 26,
        },
        "expected": 97,
    },
]


if __name__ == "__main__":
    # TestRunner(SolutionBrute().books).test(cases)
    TestRunner(SolutionOptimal().books).test(cases)
