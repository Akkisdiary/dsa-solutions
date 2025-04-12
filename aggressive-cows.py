"""
Aggressive cows
https://www.spoj.com/problems/AGGRCOW/
"""

from utils import TestRunner


class SolutionBrute:
    def cows(self, N, C, stalls):
        if C > N:
            return -1
        positions = []
        pos = []

        def solve(index, cows):
            if cows == 0:
                positions.append(pos[:])
                return
            for i in range(index, N):
                pos.append(stalls[i])
                solve(i + 1, cows - 1)
                pos.pop(-1)

        solve(0, C)

        def miniDistance(pos):
            ans = float("inf")
            for i in range(1, len(pos)):
                ans = min(ans, pos[i] - pos[i - 1])
            return ans

        for i in range(len(positions)):
            positions[i] = miniDistance(positions[i])

        return max(positions)


class SolutionOptimal:
    def cows(self, N, C, stalls):
        if C > N:
            return -1
        stalls.sort()

        high = stalls[-1] - stalls[0]
        low = 1
        while low <= high:
            mid = (low + high) // 2
            ca = self.canAssign(stalls, C, mid)
            if ca:
                low = mid + 1
            else:
                high = mid - 1
        return high

    def canAssign(self, stalls, cows, mini):
        prev = float("-inf")
        i = 0
        while cows > 0 and i < len(stalls):
            if stalls[i] - prev >= mini:
                cows -= 1
                prev = stalls[i]
            i += 1
        return cows == 0


cases = [
    {"input": {"N": 5, "C": 3, "stalls": [1, 2, 8, 4, 9]}, "expected": 3},
    {"input": {"N": 6, "C": 4, "stalls": [0, 3, 4, 7, 10, 9]}, "expected": 3},
    {"input": {"N": 5, "C": 2, "stalls": [4, 2, 1, 3, 6]}, "expected": 5},
    {"input": {"N": 3, "C": 3, "stalls": [1, 2, 3]}, "expected": 1},
    {"input": {"N": 2, "C": 3, "stalls": [1, 2]}, "expected": -1},
]

if __name__ == "__main__":
    TestRunner(SolutionBrute().cows).test(cases)
    TestRunner(SolutionOptimal().cows).test(cases)
