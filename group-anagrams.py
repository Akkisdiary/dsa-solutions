# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

from typing import List

from utils import TestRunner


class SolutionBrute:
    # time: O(n * mlogm) ; space: O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            ss = tuple(sorted(s))
            if ss not in memo:
                memo[ss] = []
            memo[ss].append(s)
        return list(memo.values())


class SolutionBetter:
    # time: O(n * m) ; space: O(n * m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            ascii_counts = [0] * 26
            for c in s:
                ascii_counts[ord(c) - ord("a")] += 1

            ascii_counts = tuple(ascii_counts)
            if ascii_counts not in memo:
                memo[ascii_counts] = []

            memo[ascii_counts].append(s)

        return memo.values()


cases = [
    {
        "input": {"strs": ["eat", "tea", "tan", "ate", "nat", "bat"]},
        "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    },
    {"input": {"strs": [""]}, "expected": [[""]]},
    {"input": {"strs": ["a"]}, "expected": [["a"]]},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().groupAnagrams).test(
        cases, lambda x: sorted([sorted(y) for y in x])
    )
    TestRunner(SolutionBetter().groupAnagrams).test(
        cases, lambda x: sorted([sorted(y) for y in x])
    )
