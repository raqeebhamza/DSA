# 
#       Company Tags                : Meta, Google
#       Leetcode Link               : https://leetcode.com/problems/count_all_valid_pickup_and_delivery_options/
# 

#********************************************* Python *******************************************************
#Time: O(n)


# Algo - Math appraoch:
# step-1 find spaces in previous combination 
# step-2 find all the possibilities for one previous res
# step-3 multiple the previous answer with currPossibility.
class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9+7
        if n == 1:
            return n
        
        res = 1
        for i in range(2,n+1):
            spaces = (i-1)*2 + 1
            currPossibility = spaces*((spaces+1)//2)
            res *= currPossibility
            res %= mod
        
        return res
        
