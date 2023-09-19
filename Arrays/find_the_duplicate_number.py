# 
#       YOUTUBE VIDEO ON THIS Qn    : https://www.youtube.com/watch?v=49HrEGt6D2s
#       Company Tags                : AMAZON
#       Leetcode Link               : https://leetcode.com/problems/find-the-duplicate-number/
# 

# NOTE : You can solve this using O(n) space, or in O(n^2) Time Complexity using double for loop to find the duplicate number
# Follow Up : How can we prove that at least one duplicate number must exist in nums? - See My Video
# Follow Up : Can you solve the problem in linear runtime complexity? - Below is the code for that

# ****************************************  Python ****************************************/
# T.C : O(n) Using "Hare & tortoise technique"
# S.C : O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = nums[0]
        fast = nums[0]
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
    
        return slow



        