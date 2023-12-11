# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Want to return array of right most element of each layer
        
        if not root:
            return []
        
        right_view = []
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            if level == len(right_view):
                right_view.append(node.val)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
                
        return right_view