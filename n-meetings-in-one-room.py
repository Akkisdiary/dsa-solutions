# N meetings in one room


# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
class Solution:
    def maximumMeetings(self, n, start, end):
        meets = [m for m in zip(start, end)]
        meets.sort(key=lambda m: m[0])
        selections = [0] * n
        count = self.find(n, meets, selections, 0, 0)
        return meets, selections

    def find(self, n, meets, selections, i, le):
        if i >= n:
            return 0
        s, e = meets[i]

        include = 0
        if s > le:
            include += 1 + self.find(n, meets, selections, i + 1, e)

        exclude = self.find(n, meets, selections, i + 1, le)

        if include > exclude:
            selections[i] = 1
            return include
        selections[i] = 0
        return exclude


class SolutionBetter:
    def maximumMeetings(self,n,start,end):
        le = -1
        count = 0
        meetings = sorted(zip(start, end), key=lambda x: x[1])
        for s, e in meetings:
            if le < s:
                count += 1
                le = e
        return count


# n = 47
# start = [86,32,31,98,37,65,98,71,99,58,59,32,52,69,15,75,4,86,57,36,83,18,58,50,43,29,98,53,80,5,89,73,8,97,17,100,9,21,55,55,32,74,60,32,87,72,54]
# end = [126,112,134,138,89,118,107,124,126,83,133,64,124,109,108,132,111,95,82,106,86,118,82,78,92,55,128,121,118,95,94,110,111,146,124,148,95,146,109,61,93,126,74,76,110,78,91]

with open("fileInput.txt", "r") as f:
    n = int(f.readline())
    start = list(map(int, f.readline().split()))
    end = list(map(int, f.readline().split()))

meets, selections = Solution().maximumMeetings(n, start, end)
print(len(list(filter(lambda s: s, selections))))
for i, selected in enumerate(selections):
    if selected:
        print(meets[i])
