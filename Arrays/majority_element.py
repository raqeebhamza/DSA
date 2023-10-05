

# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Q6L5SoS-fTo
#     Company Tags                : Amazon, Accolite, D-E-Shaw, FactSet, MakeMyTrip, Microsoft, Samsung
#     Leetcode Qn Link            : https://leetcode.com/problems/majority-element/
# 
majority_element
# ********************************************** Python **********************************************
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        maj = None

        for i in range(len(nums)):
            if count == 0:
                maj = nums[i]
                count = 1
            elif maj == nums[i]:
                count+=1
            else:
                count-=1

        return maj