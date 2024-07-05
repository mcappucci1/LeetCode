# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        result = [inf, -inf]

        prev, curr = head, head.next
        first, last = 0, 0

        while curr.next:
            minima = prev.val > curr.val < curr.next.val
            maxima = prev.val < curr.val > curr.next.val
            if minima or maxima:
                if last > 0:
                    result[0] = min(result[0], last)
                    result[1] = first
                first += 1
                last = 1
            elif last > 0:
                last += 1
                first += 1
            prev = curr
            curr = curr.next

        return result if result[0] != inf else [-1,-1]