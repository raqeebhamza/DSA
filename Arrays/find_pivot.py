# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Q0Qat25D6JE&list=PLpIkg8OmuX-K6A0sEPFxOSJh4_AjCGAFf&index=18
#     Company Tags                : Amazon, Adobe, Coupang, Radius
#     Leetcode Link               : https://leetcode.com/problems/find-pivot-index/
#     GfG Link                    : https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1/?page=1&curated[]=1&sortBy=submissions#
# 

# Approach-1 (Using O(n) space)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = [0]*len(nums)
        rightSum = [0]*len(nums)

        for i in range(1, len(nums)):
            leftSum[i] = leftSum[i-1]+nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            rightSum[i] += rightSum[i+1] + nums[i+1]

        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
                    
        return -1


# Approach-2 (Using O(1) space)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        totalSum = sum(nums)
        for i in range(len(nums)):
            if leftSum == (totalSum-leftSum-nums[i]):
                return i
            leftSum += nums[i]
        return -1