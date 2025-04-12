# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/

from utils import TestRunner


class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        content = i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                content += 1
                i += 1
            j += 1
        return content


cases = [
    {"input": {"g": [1, 2, 3], "s": [1, 1]}, "expected": 1},
    {"input": {"g": [1, 2], "s": [1, 2, 3]}, "expected": 2},
    {"input": {"g": [10, 9, 8, 7], "s": [5, 6, 7, 8]}, "expected": 2},
]


if __name__ == "__main__":
    TestRunner(Solution().findContentChildren).test(cases)
