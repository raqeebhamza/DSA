#     MY YOUTUBE VIDEO ON THIS : 
#     Company Tags             : Aamazon, Google
#     Leetcode Link            : https://leetcode.com/problems/maximum-product-subarray/

# ******************************************** Python *********************************************/
# Approach: Using prefix and suffix product

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefixProd = 1
        suffixProd = 1
        maxProd = float("-inf")
        n = len(nums)
        for i in range(len(nums)):
            if prefixProd == 0:
                prefixProd = 1
            if suffixProd == 0:
                suffixProd = 1
            prefixProd *= nums[i]
            suffixProd *= nums[n-i-1]
            maxProd = max(suffixProd, prefixProd, maxProd)
        return maxProd
