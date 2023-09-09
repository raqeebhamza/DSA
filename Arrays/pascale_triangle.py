

# 
#     Company Tags                : Amazon, Adobe, Apple
#     Leetcode Link               : https://leetcode.com/problems/pascals-triangle/
# 

#********************************************* Python ************************************************

# Time: O(N^2)
# Space: O(N^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]* (i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                res[i][j] = res[i-1][j]+res[i-1][j-1]
        
        return res
        