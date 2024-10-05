# Minimum Platforms
# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

from utils import TestRunner


class SolutionBrute:
    def minimumPlatform(self, arr, dep):
        arr = list(map(int, arr))
        dep = list(map(int, dep))
        ans = 0
        platforms = []
        trains = sorted(zip(arr, dep), key=lambda x: x[0])
        print(trains)
        for a, d in trains:
            parked = self.park(platforms, a, d)
            ans = max(ans, parked)
        return ans

    def park(self, platforms, a, d):
        i = 0
        while i < len(platforms):
            pa, pd = platforms[i]
            if pd <= a:
                platforms.pop(i)
            i += 1
        platforms.append((a, d))
        return len(platforms)


class SolutionBetter:
    def minimumPlatform(self, arr, dep):
        arr = list(map(int, arr))
        dep = list(map(int, dep))
        arr.sort()
        dep.sort()
        ans = 0
        platforms = 0
        a = d = 0
        while a < len(arr) and d < len(dep):
            if arr[a] < dep[d]:
                platforms += 1
                a += 1
            else:
                platforms -= 1
                d += 1
            ans = max(ans, platforms)
        return ans


test_cases = [
    {
        "input": {
            "arr": ["0900", "0940", "0950", "1100", "1500", "1800"],
            "dep": ["0910", "1200", "1120", "1130", "1900", "2000"],
        },
        "expected": 3,
    },
    {
        "input": {
            "arr": ["0900", "1235", "1100"],
            "dep": ["1000", "1240", "1200"],
        },
        "expected": 1,
    },
    {
        "input": {
            "arr": ["1000", "0935", "1100"],
            "dep": ["1200", "1240", "1130"],
        },
        "expected": 3,
    },
]

if __name__ == "__main__":
    TestRunner(SolutionBetter().minimumPlatform, test_cases).test()
