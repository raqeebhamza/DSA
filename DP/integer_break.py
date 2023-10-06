# /*
#     MY YOUTUBE VIDEO ON THIS Qn : Recursion + Memoization - https://www.youtube.com/watch?v=iXtqfIrWMZg
#                                   Bottom Up               - 
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/integer-break/
# */

# /****************************************************** C++ ***********************************************************/
# //Approach-1 (Recursion  + Memo)
# //T.C : O(n^2) - Because we visit at max n states and at each state we run a for loop from 1 to n-1
# //S.C : O(59) ~ O(1)

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        def solve(n):
            if n in dp:
                return dp[n]
        
            res = float("-inf")
            for i in range(1,n):
                prod = i*max(n-i,solve(n-i))
                res = max(res,prod)
            dp[n] = res
            return res
        

        return solve(n)