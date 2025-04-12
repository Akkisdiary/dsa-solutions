# Encode and Decode Strings
# https://neetcode.io/problems/string-encode-and-decode

from typing import List
from utils import TestRunner


class Solution:
    def solve(self, input: List[str]) -> List[str]:
        encoded = self.encode(input)
        return self.decode(encoded)

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lens = map(lambda s: len(s), strs)
        encoded = ",".join(map(str, lens)) + "#" + "".join(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        ans = []
        i = 0
        iend = j = s.index("#")
        while i < iend:
            n = ss = ""

            while s[i] not in (",", "#"):
                n += s[i]
                i += 1

            n = int(n)
            jj = 1
            while j + jj < len(s) and jj <= n:
                ss += s[j + jj]
                jj += 1
            ans.append(ss)
            j += n
            i += 1
        return ans


cases = [
    {
        "input": {"input": ["neet", "code", "love", "you"]},
        "expected": ["neet", "code", "love", "you"],
    },
    {
        "input": {"input": ["we", "say", ":", "yes"]},
        "expected": ["we", "say", ":", "yes"],
    },
    {"input": {"input": []}, "expected": []},
    {"input": {"input": [""]}, "expected": [""]},
]

if __name__ == "__main__":
    TestRunner(Solution().solve).test(cases)
