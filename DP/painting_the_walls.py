# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=FkJ2_hr6DRo
#     Company Tags                : GOOGLE
#     Letcode Link                : https://leetcode.com/problems/painting-the-walls/
# 


# ******************************************** Python *********************************************/
# Approach-1 (Recursion + Memo)
# T.C : O(n^2) - we will visit at max n^2 states

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        def solve(idx, remaining):
            if (idx,remaining) in dp:
                return dp[(idx,remaining)]
            if remaining <= 0:
                return 0
            if idx >= len(cost):
                return float("inf")
            
            paint = cost[idx]+solve(idx+1,remaining-1-time[idx])
            notPaint = solve(idx+1,remaining)
            dp[(idx,remaining)] =  min(paint,notPaint)
            return min(paint,notPaint)
        
        return solve(0,len(cost))

        