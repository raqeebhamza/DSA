# 
#     Company Tags                : AMAZON, GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/repeated-substring-pattern/
# 

#********************************************* Python ************************************************

# Algo:
# first take only that length through which we can create full string by append that substring.
# if (n%/)== 0: means n=12 -> l can be 1,2,3,4,6.
# times = n/l => how many times need to append.
# until l <= n/2: substring length must not greater than this.

# Time - O(n*sqrt(n))
class Solution: 
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1,(n//2)+1):
            if n%i == 0:  # <- 2*sqrt(n)
                times = n//i
                newStr = s[:i] * times # O(n)
                if newStr == s:
                    return True
        
        return False
            
                