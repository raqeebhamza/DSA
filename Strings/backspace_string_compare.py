# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=u6K3j3n3vbA
#     Company Tags                : GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/backspace-string-compare/
# 

# ******************************************************** Python ********************************************************/

# Approach-2 (Using O(1) space)
# T.C : O(max(m, n))
# S.C : O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = m-1
        j = n-1
        skips = 0
        skipt = 0
        while i >= 0 or j >=0:
            while i >= 0:
                if s[i] == "#":
                    skips+=1
                    i-=1
                elif skips>0:
                    skips-=1
                    i-=1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    skipt+=1
                    j -= 1
                elif skipt>0:
                    skipt-=1
                    j-=1
                else:
                    break
            first =  "$" if i<0 else s[i]
            second = "$" if j<0 else t[j]
            if first != second:
                return False
            i-=1
            j-=1

        return True





        