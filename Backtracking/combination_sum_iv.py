
# 
#     Company Tags                : Google, Facebook, Snapchat
#     Leetcode Link               : https://leetcode.com/problems/combination-sum-iv/
#

#******************************************* Python ****************************************************
# T.C O(N*target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        def solve(i,currSum): 
            if (i,currSum) in dp:
                return dp[(i,currSum)]
            if currSum > target:
                return 0
            if currSum == target:
                return 1
            res = 0
            for j in range(0,len(nums)):
                res += solve(j,currSum+nums[j])
            dp[(i,currSum)] = res
            return res
        
        return solve(0,0)
    