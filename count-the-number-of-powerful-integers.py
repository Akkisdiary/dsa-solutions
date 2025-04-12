# 2999. Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/?envType=daily-question&envId=2025-04-10

from utils import TestRunner


class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    ) -> int:
        return self.powerfulIntLessThan(
            str(finish), limit, s
        ) - self.powerfulIntLessThan(str(start - 1), limit, s)

    def powerfulIntLessThan(self, num: str, limit: int, suffix: str) -> int:
        prefixLen = len(num) - len(suffix)
        if prefixLen < 0:
            return 0

        ans = 0

        for i in range(prefixLen):
            n = int(num[i])
            if n <= limit:
                ans += n * (limit + 1) ** (prefixLen - i - 1)
            else:
                ans += (limit + 1) * (limit + 1) ** (prefixLen - i - 1)
                return ans

        if int(suffix) <= int(num[prefixLen:]):
            ans += 1

        return ans


cases = [
    {
        "input": {"start": 1, "finish": 6000, "limit": 4, "s": "124"},
        "expected": 5,
    },
    {
        "input": {"start": 15, "finish": 215, "limit": 6, "s": "10"},
        "expected": 2,
    },
    {
        "input": {"start": 1000, "finish": 2000, "limit": 4, "s": "3000"},
        "expected": 0,
    },
    {
        "input": {"start": 1000, "finish": 2600, "limit": 4, "s": "2500"},
        "expected": 1,
    },
    {
        "input": {"start": 1, "finish": 100, "limit": 4, "s": "100"},
        "expected": 1,
    },
    {
        "input": {"start": 1, "finish": 100, "limit": 4, "s": "101"},
        "expected": 0,
    },
    {
        "input": {"start": 1, "finish": 971, "limit": 9, "s": "71"},
        "expected": 10,
    },
    {
        "input": {"start": 1, "finish": 971, "limit": 9, "s": "72"},
        "expected": 9,
    },
    {
        "input": {"start": 20, "finish": 1159, "limit": 5, "s": "20"},
        "expected": 8,
    },
]

if __name__ == "__main__":
    TestRunner(Solution().numberOfPowerfulInt).test(cases)
