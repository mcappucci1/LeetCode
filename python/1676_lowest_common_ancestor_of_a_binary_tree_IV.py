# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        def recAncestor(root):
            if (root in nodes) or (not root):
                return root
            l = recAncestor(root.left)
            r = recAncestor(root.right)
            return root if (l and r) else (l or r)

        nodes = set(nodes)
        return recAncestor(root)