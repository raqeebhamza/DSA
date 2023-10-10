# 
#       MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=LqtcUyPBWrY
#       Company Tags                : GOOGLE
#       Leetcode Link               : https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
# 

# NOTE : The problem is the same as "get the length of the longest subarray whose difference between min and max elements is N - 1". (Make sure to remove duplicate elements)
# 
# Similar Leetcode Problems : 
# Leetcode - 658 - Find K Closest Elements - 
# Leetcode - 2779 - Maximum Beauty of an Array After Applying Operation - 
# Leetcode - 220 - Contains Duplicate III
# Leetcode - 1984 - Minimum Difference Between Highest and Lowest of K Scores
# 

# /************************************************ Python ************************************************/
# //Approach-1 (Brute Force) - TLE
# //T.C : O(n^2)
# //S.C : O(n)


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = float("inf")
        for i in range(1,2):
            L = nums[i]
            R = L + len(nums)-1

            used = set()
            operations = 0
            for j in range(len(nums)): 
                if nums[j] >= L and nums[j] <= R  and nums[j] not in used:
                    used.add(nums[j])
                    continue
                else:
                    operations += 1
            res = min(res,operations)
        
        return res

# /************************************************ Python ************************************************/
# //Approach-2 (Optimal)
# //T.C : O(nlogn)
# //S.C : O(n)
class Solution:            
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(set(nums))
        nums.sort()
        res = float("inf")
        for i in range(len(nums)):
            L = nums[i]
            R = L+len(nums)-1

            idxR = bisect.bisect(nums, R)

            withInRange = idxR-i
            outOfRange = n - withInRange

            res = min(res,outOfRange)
        
        return res



        return 0
        
