# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        front = ListNode()
        front_trav = front
        back = ListNode()
        back_trav = back
        while head:
            if head.val < x:
                front_trav.next = head
                front_trav = front_trav.next
            else:
                back_trav.next = head
                back_trav = back_trav.next
            head = head.next
        back_trav.next = None
        front_trav.next = back.next
        return front.next