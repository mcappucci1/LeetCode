# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        if not root:
            return False
        
        seen = set()
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if k - curr.val <= curr.val:
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
            elif k - curr.val > curr.val:
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            if k - curr.val in seen:
                return True
            seen.add(curr.val)
        
        return False