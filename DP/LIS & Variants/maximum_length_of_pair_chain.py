# 
#       Company Tags                : Amazon, PayU, Cisco, Zoho
#       Leetcode Link               : https://leetcode.com/problems/maximum-length-of-pair-chain/
# 

# ***************************************** Python *************************************************

#Algo: 
# step-1 sort the list because no order matters
# step-2 apply Longest increasing subsequence code recursion+memo and DP BOTTUM UP
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        dp = {}
        def LIS(prevIdx,currIdx):
            if currIdx == len(pairs):
                return 0
            
            if prevIdx !=-1 and (prevIdx,currIdx) in dp:
                return dp[(prevIdx,currIdx)]
            
            taken = 0
            if prevIdx ==-1 or pairs[currIdx][0] > pairs[prevIdx][1]:
                taken = 1 + LIS(currIdx,currIdx+1)
            
            notTaken = LIS(prevIdx,currIdx+1)
            if prevIdx != -1:
                dp[(prevIdx,currIdx)] = max(taken,notTaken)
            return max(taken,notTaken)

        pairs.sort()
        return LIS(-1,0)

