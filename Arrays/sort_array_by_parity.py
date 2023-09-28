# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=fMzddofgQOk
#       Company Tags                : META
#       Leetcode Link               : https://leetcode.com/problems/sort-array-by-parity/
# 

# ************************************************************ Python ************************************************************
# Approach-1 (Using simple iteration)
# T.C : O(n)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        
        return nums

# ************************************************************ Python ************************************************************
# Approach-2 (Writing your own custom comparator for sorting)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        sortedNums = sorted(nums, key = lambda x: x%2)

        return sortedNums