# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        # Return list of nodes that are only children
        
        # DFS
        # Iterative
        # (node, only_child)
        
        result = []
        stack = [(root, False)]
        
        while stack:
            node, only_child = stack.pop()
            if only_child:
                result.append(node.val)
            if node.left:
                stack.append((node.left, node.right == None))
            if node.right:
                stack.append((node.right, node.left == None))
        
        return result