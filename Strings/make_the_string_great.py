# 
#   MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=J43ZIltH3AY
#   Company Tags                : Google, Apple, LinkedIn, Microsoft
#   Leetcode Link               : https://leetcode.com/problems/make-the-string-great/
# 

# ********************************************************************* Python ********************************************************/
# T.C : O(n)
# S.C : O(1) -> Ignoring the space taken for result string

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for curr in list(s):
            if stack and abs(ord(curr)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr)
        return "".join(stack)
         