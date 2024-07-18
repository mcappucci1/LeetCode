# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        total = 0

        def recCountPairs(root, distance):
            if not root:
                return [0] * (distance + 1)
            if (not root.right) and (not root.left):
                return [1] + [0] * distance
            
            l = recCountPairs(root.left, distance)
            r = recCountPairs(root.right, distance)
            curr = [0] * (distance + 1)
            
            for i in range(distance):
                curr[i+1] = l[i]
            for i in range(distance):
                curr[i+1] += r[i]
            
            nonlocal total
            for i in range(distance):
                for j in range(distance):
                    if 2 + i + j <= distance:
                        total += l[i] * r[j]
            
            return curr

        recCountPairs(root, distance)
        return total