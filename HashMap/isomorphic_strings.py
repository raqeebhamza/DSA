
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=2ISNCDJEgqQ
#       Company Tags                : LinkedIn
#       Leetcode Link               : https://leetcode.com/problems/isomorphic-strings/
# 


# ****************************************** Python ******************************************/
# Using list map
# T.C : O(n)
# S.C : O(1) because list won't be greater than 26 because of 26 characters

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []
        for c in s:
            map1.append(s.index(c))
        for c in t:
            map2.append(t.index(c))
        return map1==map2
        