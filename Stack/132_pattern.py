
#
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=RZXxX1EU364
#     Company Tags                : Amazon, META
#     Leetcode Link               : https://leetcode.com/problems/132-pattern/
# 

#****************************************** Python*********************************************** 

# Approach-3 --> Using Monotonic stack
# T.C : O(n) - We don't visit any element more than once
# 
#     We are only storing one item in the stack, which is our ideal candidate for num2 (number that needs to be the largest). 
#     If we find a number that is bigger than what we thought was our ideal candidate for num2; we pop out our stack 
#     and store the value in num3 (mid value number), then we store the new ideal candidate for num2 in the stack. 
#     On the next ith iteration, if nums[i] is actually less than s3, then we are done!
# 


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # i<j<k
        # num1<num3<num2
        num3 = float("-inf")
        st = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < num3:
                return True
            while st and st[-1] < nums[i]:
                num3 = st[-1]
                st.pop()
            st.append(nums[i])
        
        return False