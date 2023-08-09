# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        trav = head
        while list1 and list2:
            if (not list2) or (list1 and list1.val <= list2.val):
                trav.next = list1
                list1 = list1.next
            else:
                trav.next = list2
                list2 = list2.next
            trav = trav.next
        if list1 or list2: trav.next = list1 or list2
        return head.next