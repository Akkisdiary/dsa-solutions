# Job Sequencing Problem
# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

from utils import TestRunner


class Job:
    # Job class which stores profit and deadline.
    def __init__(self, id, deadline, profit):
        self.id = id
        self.profit = profit
        self.deadline = deadline

    def __str__(self) -> str:
        return f"Job({self.id}, {self.deadline}, {self.profit})"

    def __repr__(self) -> str:
        return f"Job({self.id}, {self.deadline}, {self.profit})"


class Solution:
    def JobScheduling(self, Jobs: list, n):
        Jobs.sort(key=lambda j: j.profit, reverse=True)
        max_deadline = max(map(lambda j: j.deadline, Jobs))
        done = [0] * max_deadline
        for j in Jobs:
            d = j.deadline
            while d > 0 and done[d-1] != 0:
                d -= 1
            if d > 0:
                done[d-1] = j.profit
        jobs = list(filter(lambda p: p > 0, done))
        cnt = len(jobs)
        profit = sum(jobs)
        return cnt, profit


test_cases = [
    {
        "input": {
            "Jobs": [
                Job(1, 4, 20),
                Job(2, 1, 1),
                Job(3, 1, 40),
                Job(4, 1, 30),
            ],
            "n": 4,
        },
        "expected": (2, 60),
    },
    {
        "input": {
            "Jobs": [
                Job(1, 2, 100),
                Job(2, 1, 19),
                Job(3, 2, 27),
                Job(4, 1, 25),
                Job(5, 1, 15),
            ],
            "n": 5,
        },
        "expected": (2, 127),
    },
    {
        "input": {
            "Jobs": [
                Job(1, 11, 321),
                Job(2, 2, 62),
                Job(3, 5, 456),
                Job(4, 8, 394),
                Job(5, 11, 424),
                Job(6, 10, 22),
                Job(7, 1, 393),
                Job(8, 6, 87),
                Job(9, 3, 118),
                Job(10, 8, 384),
                Job(11, 10, 83),
            ],
            "n": 11,
        },
        "expected": (11, 2744),
    },
]

if __name__ == "__main__":
    TestRunner(Solution().JobScheduling, test_cases).test()
