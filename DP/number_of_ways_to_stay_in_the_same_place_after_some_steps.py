# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=NqhmQQlVhTE
#     Company Tags                : GOOGLE, META
#     Leetcode Link               : https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
# 


# ************************************************ Python ************************************************/
# Approach-1 (Using Recursion + Memo - Top Down)
# T.C : O(steps * min(steps, arrLen))


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        MOD = 10**9+7
        def solve(idx, step):   
            if (idx,step) in dp:
                return dp[(idx,step)] 
            if idx < 0 or idx >= arrLen:
                return 0
            
            if step == 0:
                return idx == 0 
            
            left = solve(idx-1,step-1)%MOD
            right = solve(idx+1,step-1)%MOD
            stay = solve(idx,step-1)%MOD

            res =  (left+right+stay)%MOD
            dp[(idx,step)] = res
            return res
        
        return solve(0,steps)
        