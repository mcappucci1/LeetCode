# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, -inf, inf)]

        while stack:
            node, lo, hi = stack.pop()
            if node.val <= lo or node.val >= hi:
                return False
            if node.left:
                stack.append((node.left, lo, node.val))
            if node.right:
                stack.append((node.right, node.val, hi))
        
        return True