"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        trav = head
        stack = []

        while trav or stack:
            if trav.child:
                if trav.next:
                    stack.append(trav.next)
                trav.child.prev, trav.next = trav, trav.child
                tmp = trav.child
                trav.child = None
                trav = tmp
            elif not trav.next and stack:
                tmp = stack.pop()
                tmp.prev, trav.next = trav, tmp
                trav = tmp
            else:
                trav = trav.next


        return head