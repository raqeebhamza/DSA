# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=HW-y3gvQTVQ
#     Company Tags                : Facebook, Uber, Google, Facebook, Microsoft
#     Leetcode Link               : https://leetcode.com/problems/decode-ways/
#     Four approaches             : Memoized, Top Down, Better Top Down, O(1) space DP
# 

# *********************************************************************** Python ***************************************************************
# Approach-1 (Using Recursion + Memoization)
# T.C : O(n) after memoization (without memoization - O(2^n)
# S.C : O(101) ~= O(1)

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        n = len(s)
        def solve(i):
            if i==n:
                return 1
            if s[i]=="0":
                return 0
            if i in dp:
                return dp[i]
            res = solve(i+1)
            if i+1 < n:
                if s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456"):
                    res+=solve(i+2)
            dp[i] = res 
            return res
        
        return solve(0)

# *********************************************************************** Python ***************************************************************
# Approach-2 (Bottom Up Way-1)
# T.C : O(n)
# S.C : O(n)
class Solution:
    def numDecodings(self, s):
        n = len(s)
        dp = [0]*(n+1)

        dp[n] = 1

        for i in range(n-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i+1 < n:
                    if s[i] == "1" or (s[i] == "2" and s[i+1]  in "0123456"):
                        dp[i] += dp[i+2]
        return dp[0]


