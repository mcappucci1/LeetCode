# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        results = []
        queue = deque([root])

        while queue:
            length = len(queue)
            results.append(-float('inf'))
            for i in range(length):
                node = queue.popleft()
                results[-1] = max(results[-1], node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return results