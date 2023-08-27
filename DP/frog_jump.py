
# 
#     Company Tags                : AMAZON, GOOGLE
#     Leetcode Link               : https://leetcode.com/problems/frog-jump/
# 

#Algo:
# step-1: Create stones to index hashmap
# step-2: Run recursion for 3 poosibilities prevJum-1,prevJump,prevJump+1 
#         and add that jump to current stone value and see if that stone exists in hashmap
# step-3: apply memoization to handle TL.


#******************************************* Python ****************************************************
#Time: O(N^2)
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stonesMap = {}
        dp = {}
        for i in range(len(stones)):
            stonesMap[stones[i]] =  i
        
        def solve(currStoneIdx, prevJump):

            if currStoneIdx == len(stones)-1:
                return True
            if (currStoneIdx,prevJump) in dp:
                return dp[(currStoneIdx,prevJump)]
            res = False
            for nxtJump in range(prevJump-1, prevJump+2):
                if nxtJump > 0:
                    nextStone = stones[currStoneIdx]+nxtJump
                    if nextStone in stonesMap:
                        res |= solve(stonesMap[nextStone],nxtJump)
            dp[(currStoneIdx,prevJump)] = res
            return res

        return solve(0,0)

