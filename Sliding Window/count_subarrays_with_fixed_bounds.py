# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=z6LwIkEn9qc
#     Company Tags                : Microsoft
#     Leetcode Link               : https://leetcode.com/problems/count-subarrays-with-fixed-bounds/
# 

# Approach-1 (Brute Force)
# Find all subarrays and check if min is minK and max is maxK
# Code will be provided soon for brute force

# Approach-2 (Optimal O(n)) - Sliding Window

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        

        culpritIdx = -1
        maxKIdx = -1
        minKIdx = -1
        res = 0

        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                culpritIdx = i
            
            if nums[i] == minK:
                minKIdx = i
            if nums[i] == maxK:
                maxKIdx = i
            
            smaller = min(maxKIdx, minKIdx)
            tmp = smaller-culpritIdx
            res +=  0 if tmp <= 0 else tmp
        
        return res