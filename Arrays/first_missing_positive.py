
# 
#     MY YOUTUBE VIDEO ON THIS QN : https://www.youtube.com/watch?v=lyjOwaUEWWQ
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/first-missing-positive/
# 

# NOTE - Using O(n) space is an easy aprproach. The followup is to use O(1) space to solve

# ******************************************************************* Python ************************************************************/
# Using O(1) space and same pattern - "Using numbers as indices"
# T.C : O(n)
# S.C : O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        containsOne = False

        for i in range(n):
            if nums[i] == 1:
                containsOne = True
            if nums[i]<=0 or nums[i] > n: # making out of bound to first index
                nums[i] = 1
        
        if not containsOne:
            return 1
        
        for i in range(n):
            num = abs(nums[i])
            idx = num-1

            if nums[idx]<0: continue
            nums[idx] *= -1
        
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1