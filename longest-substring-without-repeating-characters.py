# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# https://www.codingninjas.com/codestudio/problems/630418?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

from utils import TestRunner


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        seen = set()
        i = j = 0
        while i <= j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                seen.remove(s[i])
                i += 1
            ans = max(ans, j - i)
        return ans


cases = [
    {
        "input": {
            "s": "abcabcbb",
        },
        "expected": 3,
    },
    {
        "input": {
            "s": "bbbbb",
        },
        "expected": 1,
    },
    {
        "input": {
            "s": "pwwkew",
        },
        "expected": 3,
    },
]

if __name__ == "__main__":
    TestRunner(Solution().lengthOfLongestSubstring).test(cases)
