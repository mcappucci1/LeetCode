# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]

        while stack:
            (node, depth) = stack.pop()
            max_depth = max(max_depth, depth)
            node.right and stack.append((node.right, depth + 1))
            node.left and stack.append((node.left, depth + 1))
        
        return max_depth