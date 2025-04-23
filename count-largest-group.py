# 1399. Count Largest Group
# https://leetcode.com/problems/count-largest-group/?envType=daily-question&envId=2025-04-23

from collections import defaultdict
from utils import TestRunner


class Solution:
    # time: O(n log n) ; space: O(n)
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(list)
        for i in range(1, n + 1):
            s = sum(map(int, str(i)))
            groups[s].append(i)
        l = max(map(len, groups.values()))
        ans = 0
        for g in groups.values():
            if len(g) == l:
                ans += 1
        return ans


cases = [
    {"input": {"n": 13}, "expected": 4},
    {"input": {"n": 2}, "expected": 2},
]

if __name__ == "__main__":
    TestRunner(Solution().countLargestGroup).test(cases)
