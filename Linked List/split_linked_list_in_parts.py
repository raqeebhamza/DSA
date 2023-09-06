#
#   Asked by        : Amazon, Google
#   Leetcode Link   : https://leetcode.com/problems/split-linked-list-in-parts/
#

#**************************************** Python ********************************************

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#T.C O(L)
#S.C O(1)
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        L = 0
        curr = head
        while curr:
            L += 1
            curr = curr.next
        eachBucketNodes = L//k
        extraNodes = L%k
        res = [None]*k
        curr = head
        prev = None
        for i in range(k):
            if not curr:
                break
            res[i] = curr
            for j in range(1, eachBucketNodes+1 + (1 if extraNodes>0 else 0)):
                prev = curr
                curr = curr.next
            prev.next = None
            extraNodes -= 1
        return res
        
