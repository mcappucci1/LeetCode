# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head, prev = ListNode(0, head), None

        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        carry, head, prev = 0, prev, None

        while head:
            head.val = head.val * 2 + carry
            carry = head.val // 10
            head.val %= 10

            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        
        return prev if prev.val > 0 else prev.next