# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            curr.right, curr.left = curr.left, curr.right
            stack.append(curr.right);
            stack.append(curr.left)
        return root