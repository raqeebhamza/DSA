#
#   Asked by        : Amazon
#   Leetcode Link   : https://leetcode.com/problems/partition-list/

#************************************ Python *********************************************

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Floyd's Cycle Algorithm
# Time  : O(N)
# Space : O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return head
        
        slow = head
        fast = head.next

        while fast != slow:

            if fast == None or fast.next == None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        
        return True
        