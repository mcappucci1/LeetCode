# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def recEvaluateTree(node):
            if node.val < 2:
                return bool(node.val)
            elif node.val == 2:
                return recEvaluateTree(node.left) or recEvaluateTree(node.right)
            return recEvaluateTree(node.left) and recEvaluateTree(node.right)

        return recEvaluateTree(root)