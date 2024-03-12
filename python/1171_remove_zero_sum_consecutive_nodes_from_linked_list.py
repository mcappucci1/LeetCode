# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        stack = [(dummy, 0)]
        seen = { 0: 0 }
        trav = dummy.next
        total = 0

        while trav:
            total += trav.val
            if (total in seen) and (seen[total] < len(stack)):
                i = seen[total]
                for j in range(len(stack)-1, i, -1):
                    del seen[stack[j][1]]
                    stack.pop()
                stack[i][0].next = trav.next
            if total not in seen:
                stack.append((trav, total))
                seen[total] = len(stack)-1
            trav = trav.next

        return dummy.next