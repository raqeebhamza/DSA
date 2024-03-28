#      Scroll below to see JAVA code also    */
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=9fmKB1F1pEE
#     Company Tags                : 
#     Leetcode Link               : https://leetcode.com/problems/subarray-product-less-than-k/
# 

# ********************************************************************* Python *****************************************************************/
# Approach  : Standard Sliding window Problem
# T.C : O(N)
# S.C : O(1)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0
        
        totalCount = 0
        product = 1
        left = 0
        for right, num in enumerate(nums):
            product *= num
        
            while product >= k:
                product //= nums[left]
                left+=1
            
            totalCount += right-left+1
        
        return totalCount
        

        