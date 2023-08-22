
# 
#       Company Tags                : Facebook, Zenefits, Microsoft
#       Leetcode Link               : https://leetcode.com/problems/excel-sheet-column-title/
# 

#********************************************* Python *******************************************************
#Time: O(log(columnNumber))
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = []

        while columnNumber > 0:

            columnNumber -= 1
            remain  = columnNumber%26
            res.append(chr(remain+ord('A')))
            columnNumber //= 26
        
        return "".join(res[::-1])