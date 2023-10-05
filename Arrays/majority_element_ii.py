
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Q6L5SoS-fTo
#     Company Tags                : Amazon, Google
#     Leetcode Qn Link            : https://leetcode.com/problems/majority-element-ii/
# 

# ********************************************** Python **********************************************

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        maj1 = None

        count2 = 0
        maj2 = None
        

        for i in range(len(nums)):

            if nums[i] == maj1:
                count1+=1
            elif nums[i] == maj2:
                count2+=1
            elif count1 == 0:
                maj1 = nums[i]
                count1 = 1
            elif count2 == 0:
                maj2 = nums[i]
                count2 = 1
            else:
                count1 -=1
                count2 -=1
            
        freq1 = 0
        freq2 = 0
        for i in range(len(nums)):
            if (nums[i] == maj1):
                freq1 += 1
            elif nums[i] == maj2:
                freq2 +=1
        res = []
        if freq1 > math.floor(len(nums)/3):
            res.append(maj1)
        if freq2 > math.floor(len(nums)/3):
            res.append(maj2)
        
        return res
        