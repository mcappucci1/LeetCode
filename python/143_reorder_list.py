# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        while slow:
            n = slow.next
            slow.next = prev
            prev = slow
            slow = n
        
        dummy = ListNode()
        trav = dummy

        while prev and (head != prev):
            trav.next = head
            head = head.next
            trav = trav.next

            trav.next = prev
            prev = prev.next
            trav = trav.next

        if head == prev:
            trav.next = prev