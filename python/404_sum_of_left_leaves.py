# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left and (not node.left.left) and (not node.left.right):
                total += node.left.val
            elif node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return total