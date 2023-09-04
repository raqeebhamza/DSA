#
#     Company Tags                : AMAZON, GOOGLE, APPLE, MICROSOFT, UBER
#     Leetcode Link               : https://leetcode.com/problems/unique-paths/
# 

#********************************************* Python ************************************************
# T.C : O(N×M)
# S.C : O(N×M)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        def solve(i,j):
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i,j) in dp:
                return dp[(i,j)]
            right = solve(i,j+1)
            bottom = solve(i+1,j)
            total = right+bottom
            dp[(i,j)] = total
            return total
        
        return solve(0,0)