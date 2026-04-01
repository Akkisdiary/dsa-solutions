# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List
from utils import TestRunner


class SolutionBrute:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        mini = 0
        for i, s in enumerate(strs):
            if len(s) < len(strs[mini]):
                mini = i

        for i in range(len(strs[mini])):
            for s in strs:
                if s[i] != strs[mini][i]:
                    return pre
            pre += strs[mini][i]

        return pre


cases = [
    {
        "input": {"strs": ["flower", "flow", "flight"]},
        "expected": "fl",
    },
    {
        "input": {"strs": ["dog", "racecar", "car"]},
        "expected": "",
    },
    {"input": {"strs": ["reflower", "flow", "flight"]}, "expected": ""},
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().longestCommonPrefix).test(cases)
