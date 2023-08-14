# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        next_group = head
        curr_group = head
        head = head.next
        while next_group and next_group.next:
            next_group = next_group.next.next
            curr_group.next.next = curr_group
            curr_group.next = next_group.next if next_group and next_group.next else next_group
            curr_group = next_group
        return head
