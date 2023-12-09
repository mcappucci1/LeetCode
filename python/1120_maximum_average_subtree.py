# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:

        max_subtree = 0

        def recMaxAvgSubtree(node):
            if not node:
                return (0, 0)
            nonlocal max_subtree
            l_total, l_num_nodes = recMaxAvgSubtree(node.left)
            r_total, r_num_nodes = recMaxAvgSubtree(node.right)
            total, num_nodes = node.val + l_total + r_total, r_num_nodes + l_num_nodes + 1
            max_subtree = max(max_subtree, total / num_nodes)
            return (total, num_nodes)

        recMaxAvgSubtree(root)
        return max_subtree