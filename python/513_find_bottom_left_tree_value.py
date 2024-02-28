# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        val = -1
        q = deque([root])

        while q:
            val = q[0].val
            l = len(q)
            for i in range(l):
                node = q.popleft()
                node.left and q.append(node.left)
                node.right and q.append(node.right)
        
        return val