
# 
#     Company Tags  : Amazon, Accolite, Microsoft
#     Leetcode Link : https://leetcode.com/problems/palindromic-substrings/
# 
# ******************************************** Python *********************************************/
# Approach-1 (DP)
class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = True
            count+=1 
        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i+L-1
                if s[i] == s[j]  and L == 2:
                    dp[i][j] = True
                    count += 1
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    count += 1
        return count