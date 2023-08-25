# 
#     Company Tags                : AMAZON, GOOGLE, APPLE, MICROSOFT, UBER
#     Leetcode Link               : https://leetcode.com/problems/interleaving-string/
# 

#********************************************* Python ************************************************

#Algo: (Recursion + memoization)
# simply check if s3 (i+j)th char matches with s1 ith or s2 jth charactors
# call recursion for both options and return the response from each call with endup giving us result

# Time: O(m*n) -> len(s1)*len(s2)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        kN = len(s3)
        iN = len(s1)
        jN = len(s2)
        if kN != iN+jN:
            return False
        dp = {}
        def solve(i,j):     
            if i+j == kN and i == iN and j == jN:
                return True
            if i+j >= kN:
                return False
            if (i,j) in dp:
                return dp[(i,j)]
            res = False
            if i < iN and s1[i] == s3[i+j]:
                res = solve(i+1,j)
            if res:
                return res
            if j < jN and s2[j] == s3[i+j]:
                res = solve(i,j+1)
            dp[(i,j)] = res
            return res
        return solve(0,0)