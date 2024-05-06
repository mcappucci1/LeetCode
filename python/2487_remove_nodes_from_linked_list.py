# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Remove all nodes that have a node to the right that is larger
        # Create monotonically decreasing stack
        # Combine all nodes at the end

        stack = []

        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()
            stack.append(head)
            head = head.next
        
        dummy = ListNode()
        trav = dummy

        for node in stack:
            trav.next = node
            trav = node
        
        trav.next = None
        return dummy.next