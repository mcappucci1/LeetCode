# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        odd_level = False

        while q:
            l = len(q)
            last = inf if odd_level else -inf
            for i in range(l):
                node = q.popleft()
                if odd_level:
                    if (node.val % 2 == 1) or (node.val >= last):
                        return False
                else:
                    if (node.val % 2 == 0) or (node.val <= last):
                        return False
                last = node.val
                node.left and q.append(node.left)
                node.right and q.append(node.right)
            odd_level = not odd_level
            
        return True