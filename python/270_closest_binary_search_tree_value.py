class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) <= abs(closest - target):
                closest = root.val if abs(root.val - target) < abs(closest - target) else min(closest, root.val)
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                break
        return closest