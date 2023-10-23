
# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=-2Z4ngPy4H0
#       Company Tags                : Two Sigma
#       Leetcode Link               : https://leetcode.com/problems/power-of-four/
# 

# ******************************************************************* C++ ************************************************************************/
# Approach-1 (Simplest for loop)
# T.C : log(n) to base 4


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        while n%4 == 0:
            n //= 4
        
        if n == 1:
            return True
        return False 