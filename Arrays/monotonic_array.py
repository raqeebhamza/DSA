# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=LfYSyPP6YOA
#       Company Tags                : META (3 Times)
#       Leetcode Link               : https://leetcode.com/problems/monotonic-array/
# 

# ********************************** Python *********************************
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        decreasing = False
        increasing = False
        for i in range(len(nums)-1):

            if nums[i] < nums[i+1]:
                increasing = True
            if nums[i] > nums[i+1]:
                decreasing = True
        if decreasing and increasing:
            return False
        return True
            