# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        levels = defaultdict(list)
        q = deque([(root, 0)])
        min_level = 0

        while q:
            l = len(q)
            for i in range(l):
                node, level = q.popleft()
                min_level = min(min_level, level)
                levels[level].append(node.val)
                if node.left:
                    q.append((node.left, level-1))
                if node.right:
                    q.append((node.right, level+1))
        
        result = []
        while min_level in levels:
            result.append(levels[min_level])
            min_level += 1
        return result