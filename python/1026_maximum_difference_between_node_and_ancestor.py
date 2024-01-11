# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        max_diff = 0
        stack = [(root, root.val, root.val)]

        while stack:
            node, lo, hi = stack.pop()
            max_diff = max(max_diff, node.val - lo, hi - node.val)
            lo = min(lo, node.val)
            hi = max(hi, node.val)
            if node.left:
                stack.append((node.left, lo, hi))
            if node.right:
                stack.append((node.right, lo, hi))
        
        return max_diff