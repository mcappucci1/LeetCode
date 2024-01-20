# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        closest = None
        trav = root

        while trav != p:
            if trav.val > p.val:
                closest = trav
                trav = trav.left
            else:
                trav = trav.right

        if trav.right:
            trav = trav.right
            while trav.left:
                trav = trav.left
            return trav
        
        return closest