# 
#     MY YOUTUBE VIDEO ON THIS : Recursion + Memo -> https://www.youtube.com/watch?v=n_kL8BkURVA
#                                Bottom Up (Blue Print) -> https://www.youtube.com/watch?v=ij3X5SAhf_0
#     Company Tags             : Accolite, Amazon, Groupon, MakeMyTrip, Microsoft, Qualcomm, Samsung, Visa, Walmart, Zoho
#     Leetcode Link            : https://leetcode.com/problems/longest-palindromic-substring/
# 

# ****************************************** Python ******************************************
# Approach 1 - Recursion + Memoization
# Memoization will help reduce time complexity for cases like - "aaaaaaaaa"
# T.C : O(n^2) - Because the AMortized Time Complexity of solve() will become 1 due to memoization.
# S.C : O(n^2)
# Approach-1 (Recur + Memo)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        def solve(i, j):
            if i>=j:
                return True
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i] == s[j]:
                dp[(i,j)] = solve(i+1, j-1)
                return dp[(i,j)]
            dp[(i,j)] = False
            return dp[(i,j)]
        
        n = len(s)
        maxLen = float('-inf')
        sp = 0
        
        for i in range(n):
            for j in range(i, n):
                if solve(i,j) == True:
                    if j-i+1 > maxLen:
                        maxLen = j-i+1
                        sp = i
    
        return s[sp:sp+maxLen]
        
# ****************************************** Python ******************************************
# Approach 2 - Using Bottom Up (Elaborated for simplicity) - My favourite BluePrint for solving palindromic DP problems
# T.C : O(n^2)
# S.C : O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str: 
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        maxLen = 1 
        idx = 0
        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i+L-1
                if s[i] == s[j] and L==2:
                    dp[i][j] = True
                    maxLen = 2
                    idx = i
                elif s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 > maxLen:
                        maxLen = j-i+1
                        idx = i
                else:
                    dp[i][j] = False
        
        return s[idx:idx+maxLen]