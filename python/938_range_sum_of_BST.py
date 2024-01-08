# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        stack = [root]
        total = 0

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val
                if node.val < high and node.right:
                    stack.append(node.right)
                if node.val > low and node.left:
                    stack.append(node.left)
            elif node.val < low and node.right:
                stack.append(node.right)
            elif node.val > high and node.left:
                stack.append(node.left)
        
        return total