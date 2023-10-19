# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=ocGDVKYJKVo
#       Company Tags                : AMAZON
#       Leetcode Link               : https://leetcode.com/problems/pascals-triangle-ii/
# 

# 
#   Watch my Pascal's Triangle - I video - https://www.youtube.com/watch?v=jC0wWjBrKss
# 

# ********************************************* Python  ********************************************

# Approach-1 (Using the same code of Pascal's Triangle-I
# T.C : O(rowIndex * rowIndex)
# S.C : O(rowIndex * rowIndex)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev = []

        for i in range(rowIndex+1):
            curr = (i+1)*[1]
            for j in range(1,i):
                curr[j] = prev[j]+prev[j-1]
            prev = curr
        
        return prev