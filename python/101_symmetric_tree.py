# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        stack = [(root.right, root.left)]

        while stack:
            a, b = stack.pop()
            if (a and a.val) != (b and b.val):
                return False
            if a:
                stack.append((a.right, b.left))
                stack.append((a.left, b.right))

        return True