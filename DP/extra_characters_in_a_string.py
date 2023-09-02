# 
#       Company Tags                : Will update soon
#       Leetcode Link               : https://leetcode.com/problems/extra-characters-in-a-string/
# 


# Approach-1 (Recursion + Memo)
# T.C O(n^2)
# S.C O(n)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = {}
        dictSet = set(dictionary)
        def solve(idx):
            if idx in dp:
                return dp[idx]
            if idx >= n:
                return 0
            currStr = ""
            minExtra = n
            for i in range(idx,n):
                currStr +=  s[i]
                currExtra = len(currStr) if currStr not in dictSet else 0
                nextExtra = solve(i+1)
                totalExtra = currExtra + nextExtra
                minExtra = min(minExtra, totalExtra)
            
            dp[idx] = minExtra
            return minExtra

        return solve(0)
