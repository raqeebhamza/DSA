# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=_59HE5lVuLg
#     Company Tags  		: Amazon
#     Leetcode Link 		: https://leetcode.com/problems/min-cost-climbing-stairs/
# 

# Approach-1 (Recursion + Memo) 
# T.C : O(n) - We will visit max n states only
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def solve(idx):
            if idx >= len(cost):
                return 0
            if idx  in dp:
                return dp[idx]
            one = cost[idx] + solve(idx+1)
            two = cost[idx] + solve(idx+2)
            dp[idx] = min(one,two)
            return min(one,two)
        
        return min(solve(0),solve(1))


# Approach-2 (Bottom Up DP) Time (O(n))
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0],cost[1])
        
        for i in range(2,n):
            cost[i] =  cost[i] + min(cost[i-1], cost[i-2])
        
        return min(cost[n-1],cost[n-2])