
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=2XMBLBdgqW8
#     Company Tags                : AMAZON
#     Leetcode Link               : https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# 
maximum_score_of_a_good_subarray
# ****************************************** Python ******************************************

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        i = k
        j = k
        n = len(nums)
        currMin = nums[k]
        res = nums[k]

        while i>0 or j<n-1:
            leftVal = nums[i-1] if i>0 else 0
            rightVal = nums[j+1] if j<n-1 else 0

            if leftVal < rightVal:
                j+=1
                currMin = min(currMin, nums[j])
            else:
                i-=1
                currMin = min(currMin,nums[i])
            
            res = max(res,currMin*(j-i+1))
        
        return res
                