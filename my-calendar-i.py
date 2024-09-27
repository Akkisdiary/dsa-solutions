# 729. My Calendar I
# https://leetcode.com/problems/my-calendar-i


from utils import TestRunner


class MyCalendarBrute:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if s < end and start < e:
                return False
        self.bookings.append((start, end))
        return True


test_cases = [
    {
        "input": {
            "actions": ["MyCalendar", "book", "book", "book"],
            "input": [[], [10, 20], [15, 25], [5, 25]],
        },
        "expected": [None, True, False, True],
    },
    {
        "input": {
            "actions": ["MyCalendar", "book", "book", "book"],
            "input": [[], [10, 20], [15, 25], [5, 25]],
        },
        "expected": [None, True, False, False],
    },
    {
        "input": {
            "actions": ["MyCalendar", "book", "book", "book"],
            "input": [[], [10, 20], [25, 30], [21, 24]],
        },
        "expected": [None, True, True, True],
    },
    {
        "input": {
            "actions": ["MyCalendar", "book", "book", "book", "book", "book", "book", "book", "book", "book", "book"],
            "input": [[], [47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]],
        },
        "expected": [None, True, True, False, False, True, False, True, True, True, False],
    },
]
# TODO: Need to figure out how to test
# for case in test_cases:
#     TestRunner(SolutionOptimal().isPalindrome).case(case).test()
