class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        parents = dict()
        stack = [(root, 0)]
        p_depth, q_depth = -1, -1

        while stack and (p_depth == -1 or q_depth == -1):
            (node, depth) = stack.pop()
            if node.val == p.val:
                p_depth = depth
            elif node.val == q.val:
                q_depth = depth
            if node.left:
                parents[node.left.val] = node
                stack.append((node.left, depth + 1))
            if node.right:
                parents[node.right.val] = node
                stack.append((node.right, depth + 1))

        while p.val != q.val:
            move_p, move_q = p_depth >= q_depth, q_depth >= p_depth
            if move_p:
                p_depth -= 1
                p = parents[p.val]
            if move_q:
                q_depth -= 1
                q = parents[q.val]

        return p