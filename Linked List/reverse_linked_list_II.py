#
#   Asked by        : Amazon, Apple
#   Leetcode Link   : https://leetcode.com/problems/reverse-linked-list-ii/
#

#**************************************************************************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        sentinal = ListNode(0)
        sentinal.next = head
        prev = sentinal
        for i in range(1,left):
            prev = prev.next
        
        curr = prev.next
        for i in range(1,(right-left)+1):
            tmp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = tmp
        
        return sentinal.next

        

        