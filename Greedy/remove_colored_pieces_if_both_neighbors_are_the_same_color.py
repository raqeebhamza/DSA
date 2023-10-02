
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=8jlP3D1Dnj4
#     Company Tags                : Google
#     Leetcode Link               : https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/


# **************************************** Python ****************************************/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == colors[i] and colors[i] ==  colors[i+1]:
                if colors[i] == 'A':
                    alice+=1
                else:
                    bob+=1
        
        return alice>bob
    