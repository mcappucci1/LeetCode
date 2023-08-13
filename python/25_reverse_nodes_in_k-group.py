# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseGroup(self, head, k):
        # Check if there are at least k elements left
        i = 0
        trav = head
        while i < k and trav:
            i, trav = i + 1, trav.next
        if i != k:
            return head

        # Reverse the group
        next_group_head = self.reverseGroup(trav, k)
        end = head
        prev = None
        i = 0
        while i < k:
            i += 1
            nextt = head.next
            head.next = prev
            prev = head
            head = nextt
        end.next = next_group_head
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return head if k == 1 else self.reverseGroup(head, k)