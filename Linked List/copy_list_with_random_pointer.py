#
#   Asked by        : Amazon, Apple
#   Leetcode Link   : https://leetcode.com/problems/copy-list-with-random-pointer/
#

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# Approach - 1: Using HashMap to save the space 
#T.C O(n)
#S.C O(n) 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        newHead = None
        prev = None
        curr = head
        hm = {}
        while curr:
            tmp = Node(curr.val)
            hm[curr] = tmp
            if not newHead:
                newHead = tmp
                prev = newHead
            else:
                prev.next = tmp
                prev = tmp
            curr = curr.next
        
        
        curr = head
        newCurr = newHead

        while curr:
            if not curr.random:
                curr.random = None
            else:
                randomOriginalNode = curr.random
                newCurr.random = hm[randomOriginalNode]
            curr = curr.next
            newCurr = newCurr.next
        
        return newHead
#*********************************************************************************************
# Approach - 1: without extra space.
#T.C O(n)
#S.C O(1) 
class Solution:         
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return head
        # 1).Insert the new node in between the original linked list
        curr = head
        while curr :
            currNext = curr.next
            curr.next = Node(curr.val)
            curr.next.next = currNext
            curr = currNext
        # 2).Deep copy of random pointers
        curr = head
        while curr:
            if not curr.random:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
        
            curr = curr.next.next
        # 3). Seperate the linked Lists
        newHead = head.next
        newCurr = newHead
        curr = head
        while curr and newCurr:
            curr.next = curr.next.next if curr.next else None
            newCurr.next = newCurr.next.next if newCurr.next else None
            curr = curr.next
            newCurr = newCurr.next
        
        return newHead







