# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        height, trav = -1, root
        while trav:
            trav = trav.left
            height += 1

        h_pow = pow(2, height)
        total = h_pow - 1
        lo, hi = 0, total

        while lo <= hi:
            mid, side = (hi + lo) // 2, h_pow // 2
            trav, node_pos = root, mid
            while side > 0:
                if node_pos >= side:
                    node_pos -= side
                    trav = trav.right
                else:
                    trav = trav.left
                side //= 2
            if trav:
                lo = mid + 1
            else:
                hi = mid - 1

        return total + lo