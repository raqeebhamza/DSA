# 
#     MY YOUTUBE VIDEO ON THIS Qn : Recur+Memo & Bottom Up  - https://www.youtube.com/watch?v=SI6Pm8AKqnQ
#                                   Constant Space Solution - https://www.youtube.com/watch?v=oeYLF-u2DIA
#     Company Tags                : Amazon, OYO Rooms, Paytm, Walmart, Google, Flipkart, LinkedIn, Airbnb
#     Leetcode Link               : https://leetcode.com/problems/house-robber/
#     GfG Link                    : https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1
#     Also Famouse as             : Stickler Thief
# 


# *********************************************** Python ************************************************
# Approach-1 (Recur + Memo)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def solve(i):
            if i>=len(nums):
                return 0 
            if i in dp:
                return dp[i]
            steal = nums[i]+solve(i+2)
            skip = solve(i+1)
            currMax = max(skip, steal)
            dp[i] = currMax
            return dp[i]
        return solve(0)
# *********************************************** Python ************************************************
# Approach-2 (Bottom up)
class Solution:
    def rob(self, nums: List[int]) -> int:
        t = [0] + nums
        t[1] = nums[0]
        for i in range(2, len(t)):
            t[i] = max(nums[i-1]+t[i-2], t[i-1])
        return t[len(nums)]
# *********************************************** Python ************************************************
# Approach-3 (Bottom up) with O(1) space
class Solution:
    def rob(self, nums: List[int])->int:
        prevPrev = 0
        prev = nums[0]
        for i in range(2, len(nums)+1):
            tmp = max(prevPrev+nums[i-1],prev)
            prevPrev = prev
            prev = tmp
        return prev
