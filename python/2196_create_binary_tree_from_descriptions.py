# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:        

        root = None
        tree = { d[1]: TreeNode(d[1]) for d in descriptions }

        for p_val, c_val, isLeft in descriptions:
            if p_val not in tree:
                tree[p_val] = TreeNode(p_val)
                root = tree[p_val]
            if isLeft:
                tree[p_val].left = tree[c_val]
            else:
                tree[p_val].right = tree[c_val]
        
        return root