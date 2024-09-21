# 39. Combination Sum - https://leetcode.com/problems/combination-sum/

"""
candidates = [2,3,6,7], target = 7
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        n = len(candidates)

        def find(i, c, s):
            if s >= target:
                if s == target:
                    ans.append(c)
                return

            for j in range(i, n):
                find(j, c + [candidates[j]], s + candidates[j])

        find(0, [], 0)
        return ans


print(Solution().combinationSum([2, 3, 6, 7], 7))
