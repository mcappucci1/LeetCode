"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        p_level = 0
        q_level = 0

        trav = p
        while trav:
            p_level += 1
            trav = trav.parent

        trav = q
        while trav:
            q_level += 1
            trav = trav.parent

        while p != q:
            if p_level > q_level:
                p = p.parent
                p_level -= 1
            elif q_level > p_level:
                q = q.parent
                q_level -= 1
            else:
                p = p.parent
                q = q.parent
        
        return p