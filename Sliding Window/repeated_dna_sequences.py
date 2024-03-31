
# 
#     MY YOUTUBE VIDEO ON THIS Qn :
#     Company Tags                : 
#     Leetcode Link               : https://leetcode.com/problems/repeated-dna-sequences/
# 

# Approach-1 - Sliding Window
# T.C : O(n)
# S.C : O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        hm = {}
        res = set()
        for i in range(0,len(s)-9):

            subString = s[i:i+10]
            if subString in hm:
                res.add(subString)
            else:
                hm[subString] = True
        
        return list(res)
        

                
            