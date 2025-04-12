# 322. Coin Change – Minimum Coins to Make Sum
# https://leetcode.com/problems/coin-change/description/
# https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

from utils import TestRunner


class SolutionEasy:
    """Doesn't work where the sum of last 2 coins exceed the third coin"""

    def coinChange(self, coins, amount):
        coins.sort(reverse=True)
        ans = i = 0
        while amount > 0 and i < len(coins):
            if coins[i] <= amount:
                c = amount // coins[i]
                amount -= coins[i] * c
                ans += c
            i += 1
        if amount != 0:
            return -1
        return ans


class SolutionBrute:
    def coinChange(self, coins, amount):
        def solve(prev, rem):
            if rem < 0:
                return -1
            if rem == 0:
                return prev
            result = float("inf")
            for c in coins:
                ans = solve(prev + 1, rem - c)
                if ans >= 0:
                    result = min(result, ans)
            if result == float("inf"):
                result = -1
            return result

        return solve(0, amount)


class SolutionBetter:
    def coinChange(self, coins, amount):
        memo = {}

        def solve(prev, rem):
            if memo.get(rem) is not None:
                return memo.get(rem)
            if rem < 0:
                return -1
            if rem == 0:
                return prev
            result = float("inf")
            for c in coins:
                ans = solve(prev + 1, rem - c)
                if ans >= 0:
                    result = min(result, ans)
            if result == float("inf"):
                result = -1
            memo[amount] = result
            return result

        return solve(0, amount)


class SolutionBest:
    def coinChange(self, coins, amount):
        if amount == 0 or len(coins) == 0:
            return 0

        coins.sort()
        # print(coins)
        ans = [amount + 1] * (amount + 1)
        ans[0] = 0

        for i in range(1, len(ans)):
            j = 0
            while j < len(coins) and coins[j] <= i:
                if i - coins[j] >= 0:
                    ans[i] = min(ans[i], 1 + ans[i - coins[j]])
                j += 1
            # print(ans)
        if 0 < ans[amount] <= amount:
            return ans[amount]
        return -1


cases = [
    {"input": {"coins": [1, 5, 6, 9], "amount": 11}, "expected": 2},
    {"input": {"coins": [186, 419, 83, 408], "amount": 6249}, "expected": 20},
    {"input": {"coins": [8, 5, 4, 2], "amount": 1000}, "expected": 125},
    {"input": {"coins": [1, 2, 5], "amount": 11}, "expected": 3},
    {"input": {"coins": [2], "amount": 3}, "expected": -1},
    {"input": {"coins": [1], "amount": 0}, "expected": 0},
    {"input": {"coins": [1], "amount": 1}, "expected": 1},
    {"input": {"coins": [9, 6, 5, 1], "amount": 19}, "expected": 3},
    {"input": {"coins": [5, 1], "amount": 0}, "expected": 0},
    {"input": {"coins": [4, 6, 2], "amount": 5}, "expected": -1},
]


if __name__ == "__main__":
    TestRunner(SolutionBrute().coinChange).test(cases[:1])
    TestRunner(SolutionBetter().coinChange).test(cases[:1])
    TestRunner(SolutionBest().coinChange).test(cases[:1])
