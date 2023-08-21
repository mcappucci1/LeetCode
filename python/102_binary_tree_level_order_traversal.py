# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        levels = []
        q = deque([(root, 1)])

        while q:
            (node, level) = q.popleft()
            if len(levels) < level:
                levels.append([])
            levels[-1].append(node.val)
            node.left and q.append((node.left, level + 1))
            node.right and q.append((node.right, level + 1))

        return levels