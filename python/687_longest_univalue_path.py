# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        longest_path = 0

        def recLongest(node, parent):
            if not node:
                return 0
            l = recLongest(node.left, node.val)
            r = recLongest(node.right, node.val)
            nonlocal longest_path
            longest_path = max(longest_path, l + r)
            return (max(l, r) + 1) if node.val == parent else 0 

        recLongest(root, None)
        return longest_path