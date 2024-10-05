# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

from utils import TestRunner


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for s in s1:
            freq[s] = freq.get(s, 0) + 1
        i = j = 0
        while i <= j < len(s2):
            if s2[j] in freq:
                freq[s2[j]] -= 1
                if freq[s2[j]] == 0:
                    freq.pop(s2[j])
                j += 1
            elif i < j:
                freq[s2[i]] = freq.get(s2[i], 0) + 1
                i += 1
            else:
                i += 1
                j += 1
            if len(freq) == 0:
                return True
        return False


test_cases = [
    {
        "input": {
            "s1": "ab",
            "s2": "eidbaooo",
        },
        "expected": True,
    },
    {
        "input": {
            "s1": "ab",
            "s2": "eidboaoo",
        },
        "expected": False,
    },
    {
        "input": {
            "s1": "adc",
            "s2": "dcda",
        },
        "expected": True,
    },
    {
        "input": {
            "s1": "hello",
            "s2": "ooolleoooleh",
        },
        "expected": False,
    },
]

if __name__ == "__main__":
    TestRunner(Solution().checkInclusion, test_cases).test()
