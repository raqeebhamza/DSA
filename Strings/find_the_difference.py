
# /*
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=eWoaue1y-Cc
#     Company Tags                : AMAZON, Generally asked in short Phone Inteviews
#     Leetcode Link               : https://leetcode.com/problems/find-the-difference/

# **************************************** Python **************************************************/
# Approach-1
# T.C : Linear
# S.C : Extra space map
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hm = defaultdict()
        for e in s:
            if e not in hm:
                hm[e] = 1
            else:
                hm[e]+=1
        for e in t:
            if e not in hm:
                return e
            else:
                hm[e]-=1
                if hm[e]<0:
                    return e
        return 'x' # it won't come here

# **************************************** Python **************************************************/
# Approach-2 (Using Sum Difference)
# T.C : Linear
# S.C : constant
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sumS,sumT = 0,0
        for e in s:
            sumS += ord(e)
        for e in t:
            sumT += ord(e)
            #sumT>sumS
        return chr(sumT-sumS)

# **************************************** Python **************************************************/
# Approach-3 (Using XOR property)
# T.C : Linear
# S.C : constant
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for e in s:
            xor ^= ord(e)
        for e in t:
            xor ^= ord(e)
        return chr(xor)

