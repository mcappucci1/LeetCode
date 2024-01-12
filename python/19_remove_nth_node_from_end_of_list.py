# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        trav = dummy
        for i in range(n):
            trav = trav.next
        
        remove_next = dummy
        while trav.next:
            trav = trav.next
            remove_next = remove_next.next
        
        remove_next.next = remove_next.next.next

        return dummy.next