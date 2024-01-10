# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        max_distance = 0

        def recAmountTime(node):
            depth = 0
            if not node:
                return depth

            nonlocal max_distance
            left_depth = recAmountTime(node.left)
            right_depth = recAmountTime(node.right)

            if node.val == start:
                max_distance = max(left_depth, right_depth)
                depth = -1
            elif left_depth >= 0 and right_depth >= 0:
                depth = max(left_depth, right_depth) + 1
            else:
                distance = abs(left_depth) + abs(right_depth)
                max_distance = max(max_distance, distance)
                depth = min(left_depth, right_depth) - 1

            return depth

        recAmountTime(root)
        return max_distance