"""
Word Break II
https://www.naukri.com/code360/problems/983635
"""

from typing import Set

from utils import TestRunner


class SolutionBrute:
    def wordBreak(self, s: str, dictionary: Set):
        ans = []
        sentence = []

        def solve(start: int):
            if start == len(s):
                ans.append(" ".join(sentence[:]))
                return
            for end in range(start, len(s)):
                if s[start : end + 1] in dictionary:
                    sentence.append(s[start : end + 1])
                    solve(end + 1)
                    sentence.pop(-1)

        solve(0)
        return ans


cases = [
    {
        "input": {
            "s": "godisnowherenowhere",
            "dictionary": {"god", "is", "now", "no", "where", "here"},
        },
        "expected": [
            "god is no where no where",
            "god is no where now here",
            "god is now here no where",
            "god is now here now here",
        ],
    },
    {
        "input": {
            "s": "godisnowhere",
            "dictionary": {"god", "is", "no", "here"},
        },
        "expected": [],
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().wordBreak).test(cases, sorted)
