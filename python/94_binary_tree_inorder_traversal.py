# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        dfs = []

        while dfs or root:
            while root:
                dfs.append(root)
                root = root.left
            root = dfs.pop()
            inorder.append(root.val)
            root = root.right

        return inorder