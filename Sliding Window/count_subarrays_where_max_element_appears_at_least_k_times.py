#     Scroll below to see JAVA code also   
# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=06VaWkj8e-0
#       Company Tags                : will update soon
#       Leetcode Link               : https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
# 


# ***************************************************************************** C++ ***************************************************************
# Approach-1 (Classic sliding window)
# T.C : O(n)
# S.C : O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        maxNum = nums[0]
        for n in nums:
            maxNum = max(n,maxNum)
        res = 0
        maxWindowK = 0
        start = 0
        for end in range(len(nums)):
            if nums[end] == maxNum:
                maxWindowK += 1
            while maxWindowK == k:
                if nums[start] == maxNum:
                    maxWindowK -= 1
                start += 1
            res += start
        return res