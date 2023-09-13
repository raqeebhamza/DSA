
# 
#     Company Tags                : Amazon
#     Leetcode Link               : https://leetcode.com/problems/candy/
# 


# ***************************************** Python ******************************************************
# Approach-1 
# T.C : O(n)
# S.C : O(n) - Using only 1 Extra Array
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i]  =  max(res[i], 1 + res[i-1])

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]> ratings[i+1]:
                res[i] = max(res[i], 1 + res[i+1])

        return sum(res)
        
# ***************************************** Python ******************************************************
# Approach-2
# T.C : O(n)
# S.C : O(1)
class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        candy = n # each person given one candy

        i = 1
        while i<n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            peak = 0

            while ratings[i] > ratings[i-1]:
                peak += 1
                candy += peak
                i += 1
                if i == n:
                    return candy
            dip = 0
            while i< n and ratings[i] < ratings[i-1]:
                dip += 1
                candy += dip
                i += 1
            
            candy -= min(peak,dip)
        
        return candy
            
        