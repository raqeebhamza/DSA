
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=tWhboGihflM
#     Company Tags  		: Google, HyperVerge
#     Leetcode Link 		: https://leetcode.com/problems/constrained-subsequence-sum/ 
#     Please also see "Leetcode - 239 Sliding Window Maximum"  Both are similar to a great extent and this is the hard version.
# 

# ******************************************************* Python ******************************************************/
# Approach-1 (Recursion+Memo) Similar to LIS - TLE (18 / 25 test cases passed)
# 
# 	You should always start from an approach like this for 
# 	any DP problem.
# 



# Approach-2 (Using Priority_queue) Accepted
# 
# 	Basically in Approach-3, you want the maximum value in the range of [i, i-k]
# 	Why not store them in max heap and access them in one go
# 
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [(-nums[0], 0)]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            while i - heap[0][1] > k:
                heapq.heappop(heap)

            curr = max(0, -heap[0][0]) + nums[i]
            ans = max(ans, curr)
            heapq.heappush(heap, (-curr, i))

        return ans