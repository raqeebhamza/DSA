

# Leetcode Link   : https://leetcode.com/problems/sliding-window-maximum/
# Asked by        : Microsoft, Amazon, Google, Meta, Bloomberg

#**************************************** Python *************************************************



#Algo: Need to optimize, We can use monotonic increasing/decreasing queue
# SUDOCODE
#------ Iterate over the list and maintain a monotonic decreasing queue
#------ First check left most in queue is in window if not then remove it from queue
#------ Then while nums[i] > queue[-1]: pop from end  and then then add after loop over
#------ append the max from left most element of queue res.append(queue[0])

# Approach  : Standard Sliding window Problem
# T.C : O(n) Using monotonic decreasing deque
# S.C : O(n)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        res = []
        for i in range (len(nums)):
            if not queue:  # first time only append
                queue.append(i)
            else:
                if i-k >= queue[0]: # removing the non windows elements
                    queue.popleft()
                while queue and nums[queue[-1]]<nums[i]: # maintaing the decreasing order.
                    queue.pop() # removing the smaller elements
                queue.append(i)

            if i>=k-1: # start eppend in res only when we reached to window size.
                res.append(nums[queue[0]])
        return res
            