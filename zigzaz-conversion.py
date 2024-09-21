# 6. Zigzag Conversion - https://leetcode.com/problems/zigzag-conversion/
s = "AKSHAYSHEGAONKARSUDHIR"
numRows = 5
"""
0  A   E   S
1  K  HG  RU
2  S S A A D
3  HY  OK  HR
4  A   N   I
"""
# nextCol = currentCol + (2*numRows - 2) # 8


s = "AKSHAYSHEGAONKARSUDHIR"
numRows = 4
"""
A  S  N  D
K YH OK UH
SA EA AS I
H  G  R  R
"""
"ASNDKYHOKUHSAEAASIHGRR"
# nextCol = 2*numRows - 2 # 6

s = "PAYPALISHIRING"
numRows = 3
"""
P   A   H   N
A P L S I I G
Y   I   R
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)

        zigzag = ""
        offset = max(1, (2 * numRows - 2))
        for row in range(numRows):
            currentIdx = row
            while currentIdx < n:
                zigzag += s[currentIdx]

                nextIdx = currentIdx + offset
                midIdx = nextIdx - 2 * row

                if midIdx < n and currentIdx < midIdx < nextIdx:
                    zigzag += s[midIdx]

                currentIdx = nextIdx

        return zigzag


print(Solution().convert("A", 1))
