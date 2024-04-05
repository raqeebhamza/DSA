
#     MY YOUTBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=uzP77oJVLos
#     Company Tags               : will update soon
#     Leetcode Link              : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# 

# ****************************************************************** C++ ***********************************************************************/
# Approach-1 (using stack)
# T.C : O(n)
# S.C : O(n)

class Solution:
    def maxDepth(self, s: str) -> int:
        openBracket = 0
        res = 0
        for c in s:
            if c == "(":
                openBracket += 1
            elif c == ")":
                openBracket -= 1
            res = max(res, openBracket)
        return res