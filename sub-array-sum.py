# Q. Sub array sum


class Solution:
    def subArraySum(self, arr, n, s):
        curr_sum = arr[0]
        s = 0
        e = 1
        while e <= n:
            while curr_sum > s and s < e:
                curr_sum -= arr[s]
                s += 1

            if curr_sum == s:
                return [s + 1, e]

            if e < n:
                curr_sum += arr[e]
            e += 1

        return [-1]


print(Solution().subArraySum([4, 2, 6, 4, 0, 6, 0, 8, 1, 10], 10, 22))
