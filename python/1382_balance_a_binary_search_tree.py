# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        inorder = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        
        def recBalance(arr, l, r):
            if l > r:
                return None
            m = (r + l) // 2
            left = recBalance(arr, l, m-1)
            right = recBalance(arr, m+1, r)
            node = TreeNode(arr[m], left, right)
            return node
        
        return recBalance(inorder, 0, len(inorder)-1)