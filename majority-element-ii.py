# 229. Majority Element II
# https://leetcode.com/problems/majority-element-ii/description/


class SolutionOptimal:
    def majorityElement(self, nums):
        e1, e2 = None, None
        c1, c2 = 0, 0

        for n in nums:
            if c1 == 0 and e2 != n:
                e1 = n
                c1 += 1
            elif c2 == 0 and e1 != n:
                e2 = n
                c2 += 1
            elif e1 == n:
                c1 += 1
            elif e2 == n:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0
        for n in nums:
            if n == e1:
                c1 += 1
            if n == e2:
                c2 += 1

        ans = []
        if c1 > len(nums) // 3:
            ans.append(e1)
        if c2 > len(nums) // 3:
            ans.append(e2)
        return ans


test_cases = [
    # (input, expected_output),
    ([3, 2, 3], [3]),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([3, 3, 4], [3]),
    ([2, 2, 1, 3], [2]),
    ([2, 2], [2]),
    ([0, 0, 0], [0]),
]
for input, expected in test_cases:
    ans = SolutionOptimal().majorityElement(input)
    if ans != expected:
        print(f"FAILED: {input=}")
        print(f"{ans=}")
        print(f"{expected=}")
