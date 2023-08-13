# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Space O(log(k)), Time O(log(k) * n)
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        head = ListNode()
        trav = head
        while left and right:
            if (not right) or (left and left.val < right.val):
                trav.next = left
                left = left.next    
            else:
                trav.next = right
                right = right.next
            trav = trav.next
        trav.next = left or right
        return head.next 