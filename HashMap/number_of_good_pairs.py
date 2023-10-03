# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=RSu9uQ-OGb0
#     Company Tags                : META
#     Leetcode Link               : https://leetcode.com/problems/number-of-good-pairs/
# 

# ********************************************************* Python *********************************************************
# Approach-1 (Using simple double for loop and counting good pairs)
# T.C : O(n^2)
# S.C : O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):

                if nums[i]==nums[j]:
                    res+=1
        return res
        
# Approach-2 (Using hashmap)
# T.C : O(n) - Two Times Traversing
# S.C : O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        hm = defaultdict(int)
        for e in nums:
            hm[e] +=1
        for k,v in hm.items():
            count = hm[k]
            res += (count*(count-1))//2
        return res

# Approach-3 (Using hashmap)
# T.C : O(n) - One Time Traversing
# S.C : O(1)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        res = 0 
        for e in nums:
            res += hm[e]
            hm[e] += 1
        return res


