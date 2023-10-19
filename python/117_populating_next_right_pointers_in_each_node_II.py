"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root

        def dfs(node, right):
            node.next = right
            if (not node.left) and (not node.right):
                return
            while right and (not right.left) and (not right.right):
                right = right.next
            new_right = right and (right.left or right.right)
            if node.right:
                dfs(node.right, new_right)
            if node.left:
                dfs(node.left, node.right or new_right)


        dfs(root, None)
        return root