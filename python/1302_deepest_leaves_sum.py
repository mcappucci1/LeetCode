# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        sums = []
        stack = [(root, 0)]
        
        while stack:
            (node, level) = stack.pop()
            if level == len(sums):
                sums.append(0)
            sums[level] += node.val
            node.left and stack.append((node.left, level + 1))
            node.right and stack.append((node.right, level + 1))
            
        return sums[-1]