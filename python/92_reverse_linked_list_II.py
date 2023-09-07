# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head

        dummy = ListNode(0, head)
        before_start, after_end = dummy, head

        for i in range(right - left):
            after_end = after_end.next
        for i in range(left - 1):
            before_start = before_start.next
            after_end = after_end.next
        if after_end:
            after_end = after_end.next
    
        prev = after_end
        trav = before_start.next
        while not trav == after_end:
            nextt = trav.next
            trav.next = prev
            prev = trav
            trav = nextt

        before_start.next = prev

        return dummy.next