#     Scroll down to see JAVA code also    
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=NNxaYz0nrk0
#     Company Tags  : Facebook, Amazon, Bloomberg, Google, tiktok, Adobe
#     Frequency     : Facebook(111), Amazon(7), Bloomberg(4), Google(3), tiktok(2), Adobe(2) - I got this information from my friends. Please verify
#     Leetcode Link : https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 

# **************************************************************************** python *********************************************************************
# Approach-1 (Iterate from front and eliminate and then iterate from back and eliminate)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        cntOpen = 0
        for c in s:
            if c >= 'a' and c <= 'z':
                res += c
            elif c == '(':
                cntOpen += 1
                res += c
            elif c == ')':
                if cntOpen>0:
                    res += c
                    cntOpen -=1
        s = res
        close = 0
        res = ""
        for c in reversed(s):
            if c >= 'a' and c <= "z":
                res = c+res
            elif c == ')':
                close += 1
                res = c+res
            elif c == '(':
                if close > 0:
                    res = c + res
                    close -=1
        return res


            

