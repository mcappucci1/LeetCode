# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_index = dict()

        for i in range(len(inorder)):
            in_index[inorder[i]] = i

        def build(l, r):
            if l > r:
                return None

            root = postorder.pop()
            root_index = in_index[root]

            node = TreeNode(root)
            node.right = build(root_index + 1, r)
            node.left = build(l, root_index - 1)

            return node
        
        return build(0, len(inorder)-1)