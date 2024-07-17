# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        def recDelNodes(node, delete, roots):
            if (not node) or (len(delete) == 0):
                return node
            node.left = recDelNodes(node.left, delete, roots)
            node.right = recDelNodes(node.right, delete, roots)
            if node.val in delete:
                delete.remove(node.val)
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                node = None
            return node
    
        forest = []
        root = recDelNodes(root, set(to_delete), forest)
        if root:
            forest.append(root)
        
        return forest