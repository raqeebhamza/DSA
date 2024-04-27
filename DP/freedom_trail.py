
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=rkAvrFycfIs
#     Company Tags                : Google
#     Leetcode Link               : https://leetcode.com/problems/freedom-trail
# 


# *********************************************** Python ************************************************
# Approach-1 (Recursion  + Memoization)
# T.C : Without Memoization : O(n^m), where n is the length of the ring string and m is the length of the key string. This is because for each character in the key, 
#                              the algorithm will explore all possible positions in the ring string recursively, without reusing any previous results.
#         With Memoization  : O(n^2 * m)
# S.C : O(101*101) ~ O(1)

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def countSteps(ringIdx, i):
            dist = abs(i-ringIdx)
            wrapArround = len(ring)-dist
            return min(dist, wrapArround)
        
        dp = {}
        def solve(ringIdx, kIdx):
            if kIdx == len(key):
                return 0
            if (ringIdx, kIdx) in dp:
                return dp[(ringIdx, kIdx)]
            res = float("inf")
            for i in range(len(ring)):
                if ring[i] == key[kIdx]:
                    step = 1 + countSteps(ringIdx,i)
                    totalSteps = step+solve(i,kIdx+1)
                    res = min(res, totalSteps)
            dp[(ringIdx, kIdx)] = res
            return res

        return solve(0,0)

