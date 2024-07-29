
# 
#     MY YOUTUBE VIDEO ON THIS Qn : Recur + Memo - https://www.youtube.com/watch?v=5AxMZBirNKo
#                                   Bottom Up - https://www.youtube.com/watch?v=Sobml7FprQ0
#                                   Constant Space - https://www.youtube.com/watch?v=OyX8uPu7LvU
#     Company Tags                : Airbnb, Microsoft
#     Leetcode Link               : https://leetcode.com/problems/house-robber-ii/
# 

# *********************************************** Python ************************************************
# Approach-1 (Recur + Memo)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = {}
        def solve(i, n):
            if i>n:return 0
            
            if i in dp:
                return dp[i]
            
            steal = nums[i]+solve(i+2,n)
            skip = solve(i+1,n)
            dp[i] = max(steal, skip)
            return dp[i]
        
        taking0th = solve(0,len(nums)-2)
        dp = {}
        taking1th = solve(1, len(nums)-1)
        return max(taking0th, taking1th)
# Approach-2 (Using Bottom Up similar to House Robber-1 and just taking two cases
# 
#     Case-1 (Take from 1st House - Hence skip the last house)
#     Case-2 (Take from 2nd House - Hence take the last house)
# 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        t = [0]*(n+1)

        for i in range(1,len(nums)):
            t[i] = max(t[i-1], nums[i-1] + (t[i-2] if i-2 >=0 else 0))
        
        res1 = t[n-1]
        t = [0]*(n+1)
        for i in range(2,len(nums)+1):
            t[i] = max(t[i-1], nums[i-1]+ (t[i-2] if i-2 >=0 else 0))
        
        res2 = t[n]
        return max(res1, res2)


