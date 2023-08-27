# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        leftToRight = True
        result = []
        stack = [root]

        while stack:
            result.append([])
            next_stack = []
            for i in range(len(stack)-1, -1, -1):
                result[-1].append(stack[i].val)
                if leftToRight:
                    stack[i].left and next_stack.append(stack[i].left)
                    stack[i].right and next_stack.append(stack[i].right)
                else:
                    stack[i].right and next_stack.append(stack[i].right)
                    stack[i].left and next_stack.append(stack[i].left)
            stack = next_stack
            leftToRight = not leftToRight
            
        return result