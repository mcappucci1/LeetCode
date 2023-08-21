# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = -float('inf')

        def recFindMaxPath(node):
            nonlocal max_sum
            if node == None:
                return 0
            max_left_path = max(0, recFindMaxPath(node.left))
            max_right_path = max(0, recFindMaxPath(node.right))
            max_sum = max(max_sum, max_left_path + max_right_path + node.val)
            return node.val + max(max_left_path, max_right_path)
        
        recFindMaxPath(root)

        return max_sum