# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        

        def recBuild(preorder, inorder):
            if (not preorder) or (not inorder):
                return (None, 0)
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            num_left = 0
            num_right = 0
            if mid != 0:
                node, num_left = recBuild(preorder[1:], inorder[:mid])
                root.left = node
            if mid != len(inorder)-1:
                node, num_right = recBuild(preorder[num_left + 1:], inorder[mid+1:])
                root.right = node
            return (root, num_left + num_right + 1)
        
        return recBuild(preorder, inorder)[0]