# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        counts = dict()
        dummy = ListNode()
        trav = dummy
        
        while head:
            if head.val not in counts:
                trav.next = ListNode(0)
                trav = trav.next
                counts[head.val] = trav
            counts[head.val].val += 1
            head = head.next
        
        return dummy.next