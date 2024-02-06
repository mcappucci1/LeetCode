# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        diameter = 0

        def recDiameter(node):
            if not node:
                return -1
            l = recDiameter(node.left) + 1
            r = recDiameter(node.right) + 1
            nonlocal diameter
            diameter = max(diameter, l + r)
            return max(l, r)
    
        recDiameter(root)
        return diameter