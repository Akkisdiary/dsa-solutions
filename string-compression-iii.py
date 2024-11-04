"""
3163. String Compression III
https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04
"""

from utils import TestRunner


class SolutionBrute:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        while i < len(word):
            char = word[i]
            count = 0
            while i < len(word) and count < 9 and word[i] == char:
                count += 1
                i += 1
            comp += f"{count}{char}"
        return comp


cases = [
    {
        "input": {
            "word": "abcde",
        },
        "expected": "1a1b1c1d1e",
    },
    {
        "input": {
            "word": "aaaaaaaaaaaaaabb",
        },
        "expected": "9a5a2b",
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().compressedString).test(cases)
