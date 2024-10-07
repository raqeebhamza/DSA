    
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=4XLzLdAE4Lc
#     Company Tags                : JP Morgan, Yelp
#     Leetcode Link               : https://leetcode.com/problems/minimum-string-length-after-removing-substrings
# 

# ************************************************** Python ********************************************
# Approach-1 
# T.C : O(n)
# S.C : O(n)
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for c in s:
            if len(stack):
                if c == 'B' and stack[-1] == 'A':
                    stack.pop()
                elif c == 'D' and stack[-1] == 'C':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return len(stack)
