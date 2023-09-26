
# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=rU5p0MRm5zU
#       Company Tags                : GOOGLE
#       Leetcode Link               : https://leetcode.com/problems/remove-duplicate-letters/
#       EXACT SAME LEETCODE Qn      : https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 

# 
#     NOTE : In this Qn, I have used the result string which is working just like a stack.
#     We push into it, we pop from it from the back (result.pop_back()). So this Qn also falls under stack category.
#     You can also solve it using stack.
# 

# ********************************************* Python *********************************************/
# Approach-1 (Using string as a stack)
# T.C : O(n) - We visit each character only once (Note that an element once popped from result is never put back)
# S.C : O(1)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        lastIndex = {}
        taken = {}
        
        for i in range(len(s)):
            lastIndex[s[i]] = i
            taken[s[i]] = False
        
        res = []
        for i in range(len(s)):
            ch = s[i]
            if taken[ch]:
                continue
            
            while len(res) and res[-1] > ch and lastIndex[res[-1]]>i:
                taken[res[-1]]=False
                res.pop()
            
            res.append(ch)
            taken[ch] = True
        
        return "".join(res)
            