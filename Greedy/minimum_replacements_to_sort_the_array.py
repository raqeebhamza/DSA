
# Companies by        : GOOGLE
# Leetcode Link       : https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

#********************************************** Python *****************************************************

#Time: O(n)
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0 
        for i in range(len(nums)-2,-1,-1):

            if nums[i] <= nums[i+1]:
                continue
            
            parts = nums[i]//nums[i+1]

            if (nums[i]%nums[i+1]) != 0:
                parts+=1
            
            operations += parts - 1
            
            nums[i] = nums[i]//parts
        
        return operations
            