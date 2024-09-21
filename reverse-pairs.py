# 493. Reverse Pairs
# https://leetcode.com/problems/reverse-pairs/description/


class SolutionBrute:
    def reversePairs(self, nums):
        paris = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    paris += 1
        return paris


class SolutionOptimal:
    def reversePairs(self, nums):
        return self.solve(nums, 0, len(nums) - 1)

    def solve(self, nums, s, e):
        if s >= e:
            return 0
        ans = 0
        mid = (s + e) // 2
        ans += self.solve(nums, s, mid)
        ans += self.solve(nums, mid + 1, e)
        ans += self.merge(nums, s, mid, e)
        return ans

    def merge(self, nums, s, m, e):
        paris = self.findParis(nums, s, m, e)
        temp = []
        i = s
        j = m + 1
        while i <= m and j <= e:
            if nums[i] < nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= m:
            temp.append(nums[i])
            i += 1
        while j <= e:
            temp.append(nums[j])
            j += 1
        for i in range(len(temp)):
            nums[s+i] = temp[i]
        return paris

    def findParis(self, nums, s, m, e):
        pairs = 0
        i = s
        j = m + 1
        while i <= m:
            while j <= e:
                if nums[i] > 2 * nums[j]:
                    j += 1
                else:
                    break
            pairs += j - m - 1
            i += 1
        return pairs


test_cases = [
    # (input, expected_output),
    ([0], 0),
    ([1, 2, 3, 4], 0),
    ([-5, -5], 1),
    ([1, 3, 2, 3, 1], 2),
    ([2, 4, 3, 5, 1], 3),
    ([9, 4, 1], 3),
    ([40, 25, 19, 12, 3, 6, 2], 15),
    ([
        233, 2000000001, 234, 2000000006, 235, 2000000003, 236,
        2000000007, 237, 2000000002, 2000000005, 233, 233, 233,
        233, 233, 2000000004
    ], 40),
]
for input, expected in test_cases:
    ans = SolutionOptimal().reversePairs(input)
    if ans != expected:
        print(f"FAILED: {input=}")
        print(f"{ans=}")
        print(f"{expected=}")
