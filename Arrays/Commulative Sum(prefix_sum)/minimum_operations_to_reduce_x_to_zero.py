
# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=w7u9sMlx7zc
#       Company Tags                : AMAZON
#       Leetcode Link               : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero
# 

#*********************************************** Python ******************************************************
# Approach - 2
# left + right = X
# left, ) sum-X (, right
# different Percpective.
# Now if we find the middle array of max size whose sum equal to Sum-X
# //Using longest subarray Sum logic
# //T.C : O(n)
# //S.C : O(n)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        n = len(nums)
        currSum = 0
        hm = {}
        hm[0] = -1
        for i in range(n):
            currSum += nums[i]
            hm[currSum] = i
        if x>currSum:
            return -1
        remainingSum = currSum-x
        longestSubArray = float("-inf")

        currSum = 0
        print(hm,remainingSum)
        for i in range(n):
            currSum += nums[i]
            findSum  = currSum-remainingSum
            if findSum  in hm:
                print(findSum)
                idx = hm[findSum]
                longestSubArray = max(i-idx,longestSubArray)
            
        return -1 if longestSubArray == float('-inf') else n-longestSubArray

#********************************************** Python ************************************************************
#Approach-1 (using recursion)
# //T.C : O(2^n) -  We take and skip each ith and jth index
# //S.C : O(1) excluding Stack space
class Solution: # Time limit exceed
    def minOperations(self, nums: List[int], x: int) -> int:
        def solve(i,j,remain,count):
            nonlocal minCount
            if remain == 0:
                minCount = min(minCount,count)
            
            if remain<0 or i>j or count >= minCount:
                return
            else:
                solve(i+1,j, remain - nums[i],count+1)
                solve(i,j-1, remain-nums[j],count+1)
        
        minCount = float('inf')
        solve(0,len(nums)-1,x,0)
        if minCount == float('inf'):
            return -1
    
        return minCount
    


        