# Palindrome Partitioning

# https://leetcode.com/problems/palindrome-partitioning/


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        n = len(s)

        def isPalindrome(p):
            if len(p) == 0:
                return False

            i = 0
            j = len(p) - 1

            while i < j:
                if p[i] != p[j]:
                    return False
                i += 1
                j -= 1

            return True

        def find(prev, substr):
            n = len(substr)

            if n == 0:
                ans.append(prev)
                return

            for j in range(n + 1):
                if isPalindrome(substr[:j]):
                    find(prev + [substr[:j]], substr[j:])

        find([], s)
        return ans


print(Solution().partition("ababa"))
