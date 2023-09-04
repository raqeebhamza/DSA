#
# Leetcode Link   : https://leetcode.com/problems/partition-list/
# Asked by        : Microsoft
#----------------------------------------------------------------------------------------------
# Time : O(n), we visit each node only once

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        small = ListNode()
        large = ListNode()
        currSmall = small
        currLarge = large
        while head:
            if head.val < x:
                currSmall.next = head
                currSmall = currSmall.next
                head = head.next
                currSmall.next = None
            else:
                currLarge.next = head
                currLarge = currLarge.next
                head = head.next
                currLarge.next = None
            
        
        currSmall.next = large.next

        return small.next