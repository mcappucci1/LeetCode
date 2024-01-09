# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        longest = 0
        stack = [(root, True, 0),(root, False, 0)]

        while stack:
            node, left, length = stack.pop()
            longest = max(longest, length)
            if left:
                if node.left:
                   stack.append((node.left, False, length+1))
                if node.right:
                    stack.append((node.right, True, 1))
            else:
                if node.right:
                   stack.append((node.right, True, length+1))
                if node.left:
                    stack.append((node.left, False, 1))
        
        return longest