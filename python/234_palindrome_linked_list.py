# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            nextt = slow.next
            slow.next = prev
            prev = slow
            slow = nextt
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True