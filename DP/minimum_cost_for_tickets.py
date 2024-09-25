

# ******************************************** Python *********************************************/
# Approach-1 (Recursion + Memo)

class Solution:
     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        def solve(d):
            if d in dp:
                return dp[d]
            if d > days[-1]:
                return 0
            if d in days:
                dp[d] = min(
                    solve(d+1) + costs[0],
                    solve(d+7) + costs[1],
                    solve(d+30) + costs[2]
                )
            else:
                dp[d] = solve(d+1)
            return dp[d]
        
        return solve(0)
        
# ******************************************** Python *********************************************/
# Approach-2 (Using Bottom Up)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1] 
        dp = [0]*(lastDay+1)
        for i in range(1, lastDay+1):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    (dp[i-1] if i-1 >= 0 else 0)+costs[0],
                    (dp[i-7] if i-7 >= 0 else 0)+costs[1],
                    (dp[i-30] if i-30 >= 0 else 0)+costs[2]
                )
        return dp[lastDay]

   