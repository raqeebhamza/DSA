
# 
#     MY YOUTUBE VIDEO ON THIS Qn : https://www.youtube.com/watch?v=Sgi2BHiW0-Q
#     Company Tags                : Google
#     Leetcode Link               : https://leetcode.com/problems/palindrome-linked-list/description
# 

# ********************************************************************** Python ***************************************************************/
# //Approach-1 (Reversing the 2nd half of the linkedlist)
# //T.C : O(n)
# //S.C : O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            currNext = curr.next
            curr.next = prev
            prev = curr
            curr = currNext
        left = head
        right = prev 
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True     

# ********************************************************************** Python ***************************************************************/
# //Approach-2 (Reversing the 1st half of the linkedlist)
# //T.C : O(n)
# //S.C : O(1)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            # ------start reversing 
            slowNext = slow.next
            slow.next = prev
            prev = slow
            slow = slowNext
            #--------------- end reversing
           
        if fast:
            slow = slow.next
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
class solutions:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def solve(node):
            nonlocal curr
            if not node:
                return True 
            res = solve(node.next)
            if node.val != curr.val:
                return False
            curr = curr.next
            return res
        curr = head
        return solve(head)