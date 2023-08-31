# 
#       Company Tags                : Atlassian, Adobe, Twitter
#       Leetcode Link               : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
# 


# Approach-1 (Using Greedy approach similar to Jump Game-II)
# TC : O(n)
# SC : O(1)

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        startEnd = [0]*(n+1)

        for i in range(len(ranges)):

            start = max(0,i-ranges[i])
            end = min(n,i+ranges[i])

            startEnd[start] = max(startEnd[start],end)

        taps = 0
        maxEnd = 0
        currEnd = 0

        for i in range(n+1):
            if i>maxEnd:
                return -1

            if i>currEnd:
                taps+=1
                currEnd = maxEnd

            maxEnd = max(maxEnd,startEnd[i])

        return taps 