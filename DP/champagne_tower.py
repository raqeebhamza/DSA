# 
#     MY YOUTUBE VIDEO ON THIS Qn : Recursion + Memo - https://www.youtube.com/watch?v=-RwOEYcsQU0
#                                   Bottom Up - https://www.youtube.com/watch?v=Emv0Q2N-3n4
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/champagne-tower/
# 

# /***************************************************** Python ****************************************************************/
# //Approach-1
# //Simple Recursion + Memoization
# //T.C : O(query_row*query_row) - We visit each state only once

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = {}
        def solve(i,j):

            if (i,j) in dp:
                return dp[(i,j)]
            if i<0 or j<0 or i<j:
                return 0.0
            
            if i==0 and j==0:
                return poured
            
            upleft = (solve(i-1,j-1)-1)/2
            upright = (solve(i-1,j)-1)/2

            if upleft < 0:
                upleft = 0.0
            if upright < 0 :
                upright = 0.0
            dp[(i,j)] = upleft+upright
            return upleft + upright
        
        return min(1.0, solve(query_row,query_glass))