
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=txSMzRMREKA
#     Company Tags                :
#     Leetcode Link               : https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/
# 

# ********************************************************************** Python **********************************************************/
# //Approach-1 (With Nested Loop - Classic Sliding Window Template)
# //T.C : O(n)
# //S.C : O(n)

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        res = 0
        start = -1
        freq = Counter()
        for end in range(len(nums)):
            
            freq[nums[end]] += 1

            while freq[nums[end]] > k:
                start += 1
                freq[nums[start]] -= 1
            
            res = max(res, end-start)
        
        return res
            