
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9L7258j-enE
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/number-of-flowers-in-full-bloom/
# 

# ******************************************* Python *******************************************

# Approach-2 (Using Binary Search)
# T.C : O((m+n) * log(n))
# S.C : O(m)

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        startTime = []
        endTime = []
        for i in range(len(flowers)):
            startTime.append(flowers[i][0])
            endTime.append(flowers[i][1])
        startTime.sort()
        endTime.sort()
        res = []
        for i in range(len(people)):
            time = people[i]
            bloomedFollowersAlready = bisect.bisect_right(startTime, time)
            diedAlready = bisect.bisect_left(endTime,time)
            res.append(bloomedFollowersAlready-diedAlready)
        return res

            
            

